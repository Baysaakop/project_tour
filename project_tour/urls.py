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

    ## Tours
    path('tours/', views.TourListView.as_view(), name='tours'),
    # path('tours/', views.tours, name='tours'),
    path('tour/<int:pk>/', views.tour, name='tour'),    

    ## Accounts
    path('profile/', accounts_views.profile, name='profile'),
    path('signup/', accounts_views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)