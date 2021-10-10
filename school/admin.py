from django.contrib import admin

from school.models import School, City, Region


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('id', 'title', 'city')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('id', 'title', 'region')


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('id', 'title')
