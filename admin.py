from django.contrib import admin

from .models import AuthClient, AuthService


class AuthServiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(AuthService, AuthServiceAdmin)


class AuthClientAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'get_service', 'ip_address', 'id', 'enabled',]

    @admin.display(ordering='service__name', description='Service')
    def get_service(self, obj):
        return obj.service.name

admin.site.register(AuthClient, AuthClientAdmin)
