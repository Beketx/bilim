from django.contrib import admin
from .models import Car, Computer, Mouse
# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['title', 'age', 'model']
    search_fields = ('title', )

@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ['university', 'user', 'title']
    search_fields = ('title', )

@admin.register(Mouse)
class MouseAdmin(admin.ModelAdmin):
    list_display = ['university', 'type_in', 'color']
    search_fields = ('color', )
