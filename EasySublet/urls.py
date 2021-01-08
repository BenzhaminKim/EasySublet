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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from RoomRental.views import home_view, room_list_view, room_detail_view,room_create_view, room_update_view, room_delete_view, my_room_list_view
from Authentication.views import login_view, logout_view
from RoomRental.api import api_room_list_view,api_room_all_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', room_list_view, name='home_view'),
    path('room/list', room_list_view, name='room_list_view'),
    path('room/myroom', my_room_list_view, name='my_room_list_view'),
    path('room/detail/<int:room_id>', room_detail_view, name='room_detail_view'),
    path('room/update/<int:room_id>', room_update_view, name='room_update_view'),
    path('room/delete/<int:room_id>', room_delete_view, name='room_delete_view'),
    path('room/create', room_create_view, name='room_create_view'),
    path('authentication/login', login_view, name='login_view'),
    path('authentication/logout', logout_view, name='logout_view'),
    path('api/room/list', api_room_list_view, name='api_room_list_view'),
    path('api/room/all', api_room_all_view, name='api_room_all_view'),
    path('api/',include('RoomRental.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    