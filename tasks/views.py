from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Must, May, Want, Rubric

from django.shortcuts import render, get_object_or_404, redirect
from .forms import MustForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail


# Create your views here.
class HomeNews(ListView):
    """
    если используются спсичные данные
    """
    model = Must
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    extra_context = {
        'title': 'Главная',
    }  # только для статичных днных

    # mixin_prop = 'Hello world'
    # paginate_by = 2  # по сколько новостей из списка выводить

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = self.get_upper('Главная страница')
        # context['mixin_prop'] = self.get_prop()
        return context

    # def get_queryset(self):
    #     """
    #     чтобы показывать только опубликованные данные
    #     :return: только опубликованные данные
    #     """
    #     return News.objects.filter(is_published=True).select_related('category')


class CreateTask(CreateView):
    form_class = MustForm
    template_name = 'tasks/add_must.html'
    # login_url = '/admin/'
    raise_exception = True
    success_url = reverse_lazy('home') # редирект на главную
