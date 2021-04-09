from django.db import models
from django.conf import settings
from django_resized import ResizedImageField


class Item(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=500)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    image = ResizedImageField(size=[230, 192], upload_to='media')
    sold = models.BooleanField(default=False)

    def __int__(self):
        return self.pk


class Contact(models.Model):
    email = models.EmailField()
    location = models.CharField(max_length=100)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    interest = models.BooleanField(default=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name