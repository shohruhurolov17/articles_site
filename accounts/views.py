from django.shortcuts import render
from django.views.generic import (CreateView, UpdateView)
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from .models import CustomUser
# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class ProfileUpdateView(UpdateView):
    form_class = CustomUserChangeForm
    template_name = 'profile_update.html'
