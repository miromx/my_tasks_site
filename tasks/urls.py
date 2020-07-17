from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('s', CreateTask.as_view(), name='s'),
]
