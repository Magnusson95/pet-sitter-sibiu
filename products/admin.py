from django.contrib import admin
from .models import Animal, Category, Service

# Register your models here.
admin.site.register(Animal)
admin.site.register(Category)
admin.site.register(Service)
