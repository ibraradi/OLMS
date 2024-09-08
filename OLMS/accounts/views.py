# accounts/views.py

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    next_page = 'login'  # Redirect to login page after logout

    def dispatch(self, request, *args, **kwargs):
        logout(request)  # Explicitly log out the user
        return super().dispatch(request, *args, **kwargs)

class ProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('profile')
    template_name = 'accounts/profile.html'

    def get_object(self):
        return self.request.user
