from django.contrib import admin
from website.models import Message, FoodItem, Category

# Register your models here.

admin.site.register(Message)

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    ordering = ('name',)
    fields = ('name', 'description', 'price', 'category', 'image')

admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(Category)
