from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('serie_sasiu', )}

admin.site.register(Product, ProductAdmin)
