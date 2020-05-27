from django.contrib import admin
from .models import Tour, TourType, Price, Itinerary, TourImage, TourComment, TourLike, TourRating 

admin.site.register(Tour)
admin.site.register(TourType)
admin.site.register(Price)
admin.site.register(Itinerary)
admin.site.register(TourImage)
admin.site.register(TourComment)
admin.site.register(TourLike)
admin.site.register(TourRating)
