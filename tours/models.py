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
    # price = models.ManyToManyField(Price)
    currency = models.CharField(choices = CURRENCY_CHOICES, max_length=5, default="$")
    duration = models.IntegerField(default=0)
    language = models.CharField(choices = LANGUAGE_CHOICES, max_length=5, default="en")    
    tour_id = models.IntegerField(default=0)
    tour_type = models.ManyToManyField(TourType, blank=True)
    includes = models.TextField(blank=True)
    notincludes = models.TextField(blank=True)
    # itinerary = models.ManyToManyField(Itinerary)
    views = models.PositiveIntegerField(default=0)
    # likes = models.PositiveIntegerField(default=0)
    # rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)    

    last_updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name    

class Itinerary(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)
    name_mn = models.CharField(max_length=60)
    name_en = models.CharField(max_length=60)
    day = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Price(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)
    people = models.IntegerField(default=0)
    price_per = models.IntegerField(default=0)
    price_total = models.IntegerField(default=0)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class TourImage(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='tourimages/')
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name 

class TourComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)    
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)        

class TourLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)       
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, blank=True, null=True)
    is_liked = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)   

class TourRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)       
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)  
