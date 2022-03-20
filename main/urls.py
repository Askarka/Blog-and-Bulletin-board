from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, re_path

from main.views import RegisterDoneView, RegisterUserView, profilePage, basic

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='flow'), name='logout'),
    path('register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('register/', RegisterUserView.as_view(), name='register'),
    re_path('^(?P<username>\w+)/$', profilePage, name='profile'),
    path('show/', basic, name='contacts'),
    ]
