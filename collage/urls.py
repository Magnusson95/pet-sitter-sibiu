from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_collage, name='view_collage')
]
