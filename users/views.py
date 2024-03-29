from re import template
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

# SIGN UP VIEW
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
