from django.urls import path

from main.views import basic

urlpatterns = [
    path('', basic, name='basic'),
]
