from django.db import models
from profiles.models import UserProfile
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class UserReview(models.Model):
    """
    Model for saving reviews
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=2, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.user.username
