from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.hashers import make_password
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', "is_teacher", "have_active")
    fieldsets = (
        ['User Info', {
            'fields': ('username', 'mpassword', "is_teacher","have_active"),
        }],

    )

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            obj.password = make_password(obj.mpassword)
        super().save_model(request, obj, form, change)


admin.site.register(UserProfile, UserProfileAdmin)
