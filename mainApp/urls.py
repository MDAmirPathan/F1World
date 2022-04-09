from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    aboutUS,
    contactUS,
    home,
    liveTiming,
    results,
    standings,
    whatsNew,
)

urlpatterns = [
    path('',home, name='home'),
    path('liveTiming/',liveTiming, name='liveTiming'),
    path('results/',results, name='results'),
    path('standings/',standings, name='standings'),
    path('whatsNew/',whatsNew, name='whatsNew'),
    path('aboutUS/',aboutUS, name='aboutUS'),
    path('contactUS/',contactUS, name='contactUS'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
