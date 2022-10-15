from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField
from django.forms import ModelForm


from.models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Point
        fields = ['title', 'slug', 'description', 'photo', 'pub_date', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Длина превышает 50 символов')
        return title


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=250)
    email = forms.EmailField(label='Email')
    content = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField(label='Введите символы')


class SendEmailForm(forms.Form):
    name = forms.CharField(label='Имя отправителя', max_length=50)
    adress = forms.EmailField(label='Email получателя')
    text = forms.CharField(label='Введите сообщение', max_length=250, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))


class WriteUpForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=50)
    last_name = forms.CharField(label='Фамилия', max_length=50)
    phone_number = forms.CharField(label='Номер телефона')
    datetime = forms.DateTimeField(label='Дата и время', input_formats=['%d/%m/%Y %H:%M'])


class CommentForm(ModelForm):
    comment = forms.CharField(label='Оставить комментарий ', widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}))

    class Meta:
        model = Comment
        fields = ('comment',)
