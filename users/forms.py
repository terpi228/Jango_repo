from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(StyleFormMixin, forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone', 'avatar','country',)

    def clean_password2(self):
        p1 = self.cleaned_data.get('password1')
        p2 = self.cleaned_data.get('password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('Пароли не совпадают')
        return p2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if hasattr(user, 'username') and not user.username:
            user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user

from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(StyleFormMixin, AuthenticationForm):
    username = forms.EmailField(label='Email')  

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'phone', 'avatar', 'country']
        widgets = {
            'email': forms.EmailInput(attrs={'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'    