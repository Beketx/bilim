from rest_framework.routers import DefaultRouter
from django.urls import path, include

from university.views import UniversityView, FacultyView

router = DefaultRouter()
router.register(r'university', UniversityView, basename='university')
router.register(r'faculty', FacultyView, basename='faculty')
