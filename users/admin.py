from django.contrib import admin
from users.models import CustomUser
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    model=CustomUser
    list_display = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)