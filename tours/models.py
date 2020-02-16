from django.db import models
from django.contrib.auth.models import User

LANGUAGE_CHOICES = {
    ("en", "English"),
    ("ja", "Japanese"),
    ("ko", "Korean"),
    ("zh-cn", "Chinese"),
}

CURRENCY_CHOICES = {
    ("$", "USD"),
    ("¥", "JPY"),
    ("₩", "KRW"),
    ("元", "RMB"),
}

class TourType(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    language = models.CharField(choices = LANGUAGE_CHOICES, max_length=5, default="en")
    type_id = models.IntegerField(default=0)

    last_updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Tour(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    duration = models.IntegerField(default=0)
    language = models.CharField(choices = LANGUAGE_CHOICES, max_length=5, default="en")
    currency = models.CharField(choices = CURRENCY_CHOICES, max_length=5, default="$")
    tour_id = models.IntegerField(default=0)
    tour_type = models.ManyToManyField(TourType, blank=True)

    last_updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
