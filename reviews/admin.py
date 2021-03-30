from django.contrib import admin
from .models import UserReview


class ReviewAdmin(admin.ModelAdmin):
    fields = ('user', 'review', 'date', 'rating')


admin.site.register(UserReview)
