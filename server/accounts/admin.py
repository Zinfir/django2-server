from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account


@admin.register(Account)
class AccountAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            'Extra', {
                'fields': ('avatar', 'phone')
            },
        ),
    )

