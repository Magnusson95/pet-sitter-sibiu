from django.db import models
from profiles.models import UserProfile
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class UserReview(models.Model):
    """
    Model for saving reviews
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=((1, (1)),
                                          (2, (2)),
                                          (3, (3)),
                                          (4, (4)),
                                          (5, (5))),
                                          default=3)
    date = models.DateTimeField(auto_now_add=True)
    review = models.TextField()

    def __str__(self):
        return self.user.username
