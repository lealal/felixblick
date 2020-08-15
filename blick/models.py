from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Listing(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField()
    bedroom = models.IntegerField(default=1)
    bathroom = models.DecimalField(max_digits=2, decimal_places=1, default=1)
    sqft = models.IntegerField()
    price = models.IntegerField()
    photo_main = models.ImageField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    isSold = models.BooleanField(default=False)
    isPending = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    repBuyer = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

class News(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True)
    description = models.TextField()
    url = models.CharField(max_length=200)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)