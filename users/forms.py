from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserOurRegistration(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        managed = True
        verbose_name = 'Юзер'
        verbose_name_plural = 'Юзеры'


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImage(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(ProfileImage, self).__init__(*args, **kwargs)
        self.fields['img'].label="Изображение профиля"

    class Meta:
        model = Profile
        fields = ['img']
