from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import JuicyView

router = DefaultRouter()
router.register(r'juicy', JuicyView, basename='juicy')

urlpatterns = [
    path('', include(router.urls))
]
