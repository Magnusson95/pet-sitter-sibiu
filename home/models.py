from django.db import models


class EmailForm(models.Model):
    """
    Model for sending emails
    """
    name = models.CharField(max_length=50, null=False, blank=False)
    message = models.TextField()
    email = models.EmailField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.name
