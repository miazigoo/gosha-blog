from django.shortcuts import render, get_object_or_404
from .models import News
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
    )
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DeleteView, 
    DetailView, 
    CreateView,
    UpdateView
    )


def contacti(request):
    return render(request, 'blog/contacti.html', {"title": "Page for us "})


class ShowNewsView(ListView):
    model=News
    template_name='blog/home.html'
    context_object_name='news'
    ordering = ['-date']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ShowNewsView,self).get_context_data(**kwargs)
        context["title"] = 'Главная страница'
        return context
    

class NewsDetailView(DetailView):
    model = News
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context["title"] = News.objects.filter(pk=self.kwargs['pk']).first()
        return context


class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    fields = ['title', 'text']
    context_object_name = 'creat'

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)


class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False



class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url='/'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False

class UserAllView(ListView):
    model=News
    template_name='blog/user_news.html'
    context_object_name='news'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(avtor=user).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(UserAllView,self).get_context_data(**kwargs)
        context["title"] = 'Статьи пользователя'
        return context