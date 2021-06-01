from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from main.forms import RegisterUserForm

User = get_user_model()
class RegisterUserView(CreateView):
    model = User
    template_name = 'registration/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('register_done')


class RegisterDoneView(TemplateView):
    template_name = 'registration/register_done.html'

def basic(request):
    return render(request, 'main/contacts.html')

@login_required #Убрать, если сломатся
def profilePage(request, username):

    return render(request, 'main/profile.html', context={'profile': request.user})
