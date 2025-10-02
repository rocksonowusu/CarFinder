from django.contrib import admin
from .models import Car
# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'name', 'price', 'car_type', 'purpose']
    list_filter = ['car_type','purpose', 'price']
    search_fields = ['brand','name']
    ordering = ['price']