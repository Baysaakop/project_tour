from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from tours import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns (
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    ## Tours
    path('tourlist/', views.TourListView.as_view(), name='tourlist'),
    path('tour/<int:pk>/', views.tour, name='tour'),    
    path('touredit/', views.touredit, name='touredit'),
    path('touradd/', views.touradd, name='touradd'),
    path('liketour/', views.likeTour, name='liketour'),
    path('ratetour/', views.rateTour, name='ratetour'),
    path('commenttour/', views.commentTour, name='commenttour'),
    # path('tours/', views.tours, name='tours'),

    ## Accounts
    path('profile/<int:id>/', accounts_views.profile, name='profile'),
    path('signup/', accounts_views.signup, name='signup'),
    path('ajax/validate_username/', accounts_views.validate_username, name='validate_username'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/edit/', accounts_views.UserUpdateView.as_view(), name='edit_profile'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)