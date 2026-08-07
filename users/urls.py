from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import RegisterView, UserLoginView, ProfileUpdateView   # ← импорт добавлен

app_name = 'users'

urlpatterns = [
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]