from django.contrib import admin

# Register your models here.

from .models import Doufu

class DoufuAdmin(admin.ModelAdmin):
    fields = ['doufu_name', 'raw_material', 'introduce', 'methods']

admin.site.register(Doufu, DoufuAdmin)