from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    fee_multiplier = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Animal(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    animal = models.CharField(max_length=254)

    def __str__(self):
        return self.animal


class Service(models.Model):
    service_type = models.CharField(max_length=254)
    period = models.DecimalField(max_digits=6, decimal_places=0)
    cost = models.DecimalField(max_digits=6, decimal_places=0)
    sub_heading = models.CharField(max_length=254)
    detail_1 = models.CharField(max_length=254)
    detail_2 = models.CharField(max_length=254)
    detail_3 = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.service_type
