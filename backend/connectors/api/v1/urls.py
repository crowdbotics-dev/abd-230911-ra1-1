from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import SSpotifyConnectorViewSet

router = DefaultRouter()
router.register("sspotify", SSpotifyConnectorViewSet, basename="sspotify-connector")

urlpatterns = [
    path("", include(router.urls)),
]
