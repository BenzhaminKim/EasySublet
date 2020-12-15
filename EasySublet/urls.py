"""EasySublet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from RoomRental.views import home_view, room_list_view, room_detail_view,room_create_view, room_update_view, room_delete_view
from Authentication.views import log_In_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('room/list', room_list_view, name='room_list_view'),
    path('room/detail/<int:room_id>', room_detail_view, name='room_detail_view'),
    path('room/update/<int:room_id>', room_update_view, name='room_update_view'),
    path('room/delete/<int:room_id>', room_delete_view, name='room_delete_view'),
    path('room/create', room_create_view, name='room_create_view'),
    path('authentication/login', log_In_view, name='log_in_view'),
]
