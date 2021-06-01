from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from main.views import RegisterDoneView, RegisterUserView

urlpatterns = [
path('accounts/login/', LoginView.as_view(), name='login'),
path('accounts/logout/', LogoutView.as_view(next_page='blog:flow'), name='logout'),
path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
path('accounts/register/', RegisterUserView.as_view(), name='register')
    ]