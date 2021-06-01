from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from blog.forms import PostForm
from blog.models import Post


def flow(request):
    posts = Post.objects.all().prefetch_related('images')
    context = {'posts': posts}
    return render(request, 'blog/flow.html', context)


class HomePageView(ListView):
    model = Post
    template_name = 'blog/flow.html'


class CreatePostView(CreateView):  # новый
    model = Post
    form_class = PostForm
    template_name = 'blog/post.html'
    success_url = reverse_lazy('home')