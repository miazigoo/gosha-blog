from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowNewsView.as_view(), name='blog-home'),
    path('user/<str:username>', views.UserAllView.as_view(), name='user_news'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/new', views.CreateNewsView.as_view(), name='news-new'),
    path('news/<int:pk>/update', views.UpdateNewsView.as_view(), name='news-update'),
    path('contacti', views.contacti, name='blog-contacti'),
    path('news/<int:pk>/delete', views.DeleteNewsView.as_view(), name='delete'),
]
