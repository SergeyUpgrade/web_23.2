from django.contrib import admin

from catalog.models import Product, Category, Version
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')


