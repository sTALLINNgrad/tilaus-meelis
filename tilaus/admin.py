from django.contrib import admin

from .models import Product, Category, Tuotesarja, Toimittaja

   

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        's_numero',
        'category',
        'tuotesarja',
        'name',
        'description',
        'toimittajan_tuotekoodi',
        'toimittaja',
        'kuva'
    )
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tuotesarja)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Toimittaja)
class CategoryAdmin(admin.ModelAdmin):
    pass