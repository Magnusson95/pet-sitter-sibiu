from django.db import models


class Collage(models.Model):
    photo_name = models.CharField(max_length=254)
    photo_description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.photo_name
