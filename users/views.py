from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserOurRegistration, UserUpdateForm, ProfileImage
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method=="POST":
        form = UserOurRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} был успешно создан! Введите имя пользователя и пароль для авторизации')
            return redirect('login')
    else:
        form = UserOurRegistration()
    return render(request, 'user/register.html', {'form': form, 'title': 'Регистрация пользователя'})


@login_required
def profile(request):
    if request.method == "POST":
        img_profile = ProfileImage(request.POST, request.FILES, instance=request.user.profile)
        update_user = UserUpdateForm(request.POST, instance=request.user)
        if update_user.is_valid() and img_profile.is_valid():
            update_user.save()
            img_profile.save()
            messages.success(request, f'Ваш профиль был успешно изменён!')
            return redirect('profile')
    else:
        img_profile = ProfileImage(instance=request.user.profile)
        update_user = UserUpdateForm(instance=request.user)
    data = {
        'img_profile': img_profile,
        'update_user': update_user
    }
    return render(request, 'user/profile.html', data)
