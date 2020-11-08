from django.contrib import admin
from .models import Animal, Category, Service

# Register your models here.


class AnimalAdmin(admin.ModelAdmin):
    list_display = (
        'animal',
        'category'
    )

    ordering = ('category', 'animal',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'fee_multiplier'
    )

    ordering = ('fee_multiplier',)


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'service_type',
        'sub_heading',
        'cost'
    )

    ordering = ('service_type',)


admin.site.register(Animal, AnimalAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
