"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as UserView
from django.contrib.auth import views as authView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")),
    path('reg/', UserView.register, name='reg'),
    path('login/', 
        authView.LoginView.as_view(template_name='user/user.html'), name='login'),
    path('logout/', 
        authView.LogoutView.as_view(template_name='user/exit.html'), name='exit'),
    path('profile/', UserView.profile, name='profile'),
    path('pass-reset/', 
        authView.PasswordResetView.as_view(template_name='user/pass_reset.html'), 
        name='pass-reset'),
    path('password_reset_confirm/<uidb64>/<token>/', 
        authView.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), 
        name='password_reset_confirm'),
    path('password-reset/done/', 
        authView.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), 
        name='password_reset_done'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    