from django.contrib import admin
from university.models import University, Faculty, Specialty


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'address')
    search_fields = ('title',)


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('title', 'university')
    search_fields = ('title',)


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('title', 'faculty')
    search_fields = ('title',)
