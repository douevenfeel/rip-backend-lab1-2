from django.contrib import admin
from .models import *

@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    pass

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    pass

@admin.register(Baskets)
class BasketsAdmin(admin.ModelAdmin):
    pass

