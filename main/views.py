from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from main.forms import RegisterUserForm


class RegisterUserView(CreateView):
    odel = User
    template_name = 'registration/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')

class RegisterDoneView(TemplateView):
    template_name = 'registration/register_done.html'

