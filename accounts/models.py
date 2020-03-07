from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

SEX_CHOICES = {
    ("m", "male"),
    ("f", "female"),
    ("u", "unidentified"),
}

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(choices = SEX_CHOICES, max_length=1, default="u")    
    birth_date = models.DateField(blank=True, null=True)
    is_moderator = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
