# Authentication/urls.py

from django.urls import path, include
from django.conf.urls import url
from .views import register

urlpatterns = [
    path('register/',register,name='register'),
    path('accounts/',include("django.contrib.auth.urls")),
]