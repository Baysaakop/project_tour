from django.contrib import admin
from .models import Tour, TourType, Price, Itinerary

admin.site.register(Tour)
admin.site.register(TourType)
admin.site.register(Price)
admin.site.register(Itinerary)
