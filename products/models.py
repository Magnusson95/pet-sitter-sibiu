from django.db import models


class Category(models.Model):
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
    period = models.DecimalField(max_digits=6, decimal_places=2)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    sub_heading = models.CharField(max_length=254)
    detail_1 = models.CharField(max_length=254)
    detail_2 = models.CharField(max_length=254)
    detail_3 = models.CharField(max_length=254)

    def __str__(self):
        return self.service_type
