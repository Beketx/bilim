from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import TestView, TestViewSet

router = DefaultRouter()
router.register(r'testviewset', TestViewSet, basename='test')

urlpatterns = [
    path('testview/', TestView.as_view(), name='testapi'),
    path('', include(router.urls))
]
