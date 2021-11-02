from django.urls import path
from . import views
from users.views import UserCreateView
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import UserLoginForm


urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html',
                                     authentication_form=UserLoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
