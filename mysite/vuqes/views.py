from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse, BadHeaderError
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView, DetailView
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser

from .forms import *
from .serializers import PointSerializer, UserSerializer
from .utils import *
from .permissions import IsAdminOrOnlyRead


class VuqesHome(DataMixin, ListView):
    model = Point
    context_object_name = 'get'
    template_name = 'vuqes/base.html'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return context | c_def


def index(request, slug):   # Оставляем комментарий + отображаем пост по слагу
    get = Point.objects.get(slug=slug)
    if request.method == 'POST':
        Comment.objects.create(comment=request.POST.get('comment'), date=timezone.now(), ident=get.slug, user=request.user)

    form = CommentForm()
    context = {
        'form': form,
        'title': 'Пост',
        'names': Comment.objects.all(),
        'user': request.user,
        'get': get,
    }
    return render(request, 'vuqes/index.html', context)


def write_up(request):
    if request.method == 'POST':
        form = WriteUpForm(request.POST)
        if form.is_valid():
            try:
                WriteToTraining.objects.create(**form.cleaned_data)
                return redirect('write')
            except:
                form.add_error(None, 'Ошибка записи! Проверьте введенные вами данные')
    else:
        form = WriteUpForm()
    context = {
        'user': request.user,
        'form': form,
        'title': 'Запись на тренировку',
        'get': WriteToTraining.objects.all(),
    }
    return render(request, 'vuqes/write.html', context)


class Move(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'vuqes/desc_2.html'
    login_url = reverse_lazy('home')
    success_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить статью')
        return context | c_def


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'vuqes/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return context | c_def

    def form_valid(self, form):  # Авторизация при успешной регистрации
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'vuqes/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return context | c_def

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):  # Выход из учетной записи
    logout(request)
    return redirect('login')


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'vuqes/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        return context | c_def

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class SendEmail(DataMixin, FormView):
    form_class = SendEmailForm
    template_name = 'vuqes/email.html'
    success_url = reverse_lazy('email')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Отправить сообщение')
        return context | c_def

    def send_email(self, request):
        if request.method == 'POST':
            form = SendEmailForm(request.POST)
            if form.is_valid():
                try:
                    send_mail(form)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return HttpResponseRedirect('email')
            else:
                return HttpResponse('Make sure all fields are entered and valid.')


def category(request):
    context = {
        'get': Point.objects.all(),
        'get_cat': Add.objects.all(),
        'title': 'Поиск по категориям',
    }
    return render(request, 'vuqes/cat.html', context)


class AboutUs(ListView):
    model = Point
    template_name = 'vuqes/about.html'
    extra_context = {'title': 'О сайте'}


def about_API(request):
    return render(request, 'vuqes/API.html', {'title': 'API'})


# Здесь представления для DRF


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
    permission_classes = (IsAdminOrOnlyRead,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class PointAPIDestroy(generics.RetrieveUpdateAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
    permission_classes = (IsAdminOrOnlyRead,)

