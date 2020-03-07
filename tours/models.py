from django.db import models
from django.contrib.auth.models import User

LANGUAGE_CHOICES = {
    ("en", "English"),
    ("ja", "Japanese"),
    ("ko", "Korean"),
}

CURRENCY_CHOICES = {
    ("$", "USD"),
    ("¥", "JPY"),
    ("₩", "KRW"),
}

class Itinerary(models.Model):
    name_mn = models.CharField(max_length=60)
    name_en = models.CharField(max_length=60)
    day = models.IntegerField(default=0)
    description = models.TextField(blank=True)

class Price(models.Model):
    people = models.IntegerField(default=0)
    price_per = models.IntegerField(default=0)
    price_total = models.IntegerField(default=0)

class TourType(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    language = models.CharField(choices = LANGUAGE_CHOICES, max_length=5, default="en")
    type_id = models.IntegerField(default=0)

    last_updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class TourImage(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='tourimages/')

    def __str__(self):
        return self.name 

class Tour(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.ManyToManyField(Price)
    currency = models.CharField(choices = CURRENCY_CHOICES, max_length=5, default="$")
    duration = models.IntegerField(default=0)
    language = models.CharField(choices = LANGUAGE_CHOICES, max_length=5, default="en")    
    tour_id = models.IntegerField(default=0)
    tour_type = models.ManyToManyField(TourType, blank=True)
    includes = models.TextField(blank=True)
    notincludes = models.TextField(blank=True)
    itinerary = models.ManyToManyField(Itinerary)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    image = models.ManyToManyField(TourImage, blank=True)

    last_updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class TourReview(models.Model):
    is_liked = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    comment = models.TextField()
    username = models.CharField(max_length=120, default="")
    email = models.EmailField(max_length=254, default="")
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)   