from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from .forms import ProfileForm
from users.models import User
from users.forms import UserRegisterForm, UserLoginForm

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user_email = form.cleaned_data.get('email')
        try:
            send_mail(
                subject='Добро пожаловать!',
                message='Вы успешно зарегистрировались на нашем сайте.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user_email],
                fail_silently=False,
            )
        except Exception as e:
            print(f'Ошибка отправки письма: {e}')
        return response


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'





