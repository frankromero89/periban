from django.contrib import admin

from menus.models import Menu, Platillo

# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

@admin.register(Platillo)
class PlatilloAdmin(admin.ModelAdmin):
    list_display = ('menu', 'name')