from django.shortcuts import render

from blog.models import Post, PostImage


def basic(request):
    return render(request, 'main/contacts.html')