from django.urls import path, include
from rest_framework import routers
from .api import RoomViewSet

router = routers.DefaultRouter()
router.register('all',RoomViewSet,'rooms')

urlpatterns = router.urls