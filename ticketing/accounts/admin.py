from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.hashers import make_password
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
    fieldsets = (
        ['用户信息', {
            'fields': ('username', 'mpassword', "avatar","is_superuser"),
        }],

    )

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            obj.password = make_password(obj.mpassword)
        super().save_model(request, obj, form, change)


admin.site.register(UserProfile, UserProfileAdmin)
