from django.urls import path
from .views import *

urlpatterns = [
    path('', VuqesHome.as_view(), name='home'),
    path('<slug:slug>/', index, name='index'),
    path('/write/', write_up, name='write'),
    path('/move/', Move.as_view(), name='move'),
    path('/register/', RegisterUser.as_view(), name='register'),
    path('/login/', LoginUser.as_view(), name='login'),
    path('/logout/', logout_user, name='logout'),
    path('/contact/', ContactFormView.as_view(), name='contact'),
    path('/email/', SendEmail.as_view(), name='email'),
    path('/cat/', category, name='cat'),
    path('/about/', AboutUs.as_view(), name='about'),
    path('/API/', about_API, name='API')
]
