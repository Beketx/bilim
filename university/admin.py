from django.contrib import admin
from university.models import GrantPoint, University, Faculty, Specialty


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'address', 'image')
    search_fields = ('title',)


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('title', 'faculty')
    search_fields = ('title',)

@admin.register(GrantPoint)
class GrantPointAdmin(admin.ModelAdmin):
    list_display = ('subject_first', 'subject_second', 'point', 'specialty')
    search_fields = ('specialty',)

