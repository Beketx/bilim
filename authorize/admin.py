from django.contrib import admin
from authorize.models import User, UserToken, UserActivation, Profile


@admin.register(UserActivation)
class UserActivationAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'created_at', 'activated_at')
    fields = ('user', 'code', 'created_at', 'activated_at')
    list_filter = ()
    readonly_fields = ('pk', 'created_at')
    search_fields = ('user__phone', 'user__email', 'user__full_name')

#123
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'is_active', 'created_at')
    fields = (
        'email', 'full_name', 'phone', 'photo', 'is_active', 'is_admin',
        'created_at', 'password')
    list_filter = ()
    readonly_fields = ('pk',)
    search_fields = ('email', 'phone', 'full_name')

    def save_model(self, request, obj, form, change):
        if obj.pk:
            orig_obj = User.objects.get(pk=obj.pk)
            if obj.password != orig_obj.password:
                obj.set_password(obj.password)
        else:
            obj.set_password(obj.password)
        obj.save()


@admin.register(UserToken)
class UserTokenAdmin(admin.ModelAdmin):
    search_fields = ('user__email',)
    list_display = ('user', 'user_agent', 'ip_address')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('user__email',)
    list_display = ('user', 'school')
