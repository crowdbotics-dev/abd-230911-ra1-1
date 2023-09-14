from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import FreeDogAPIConnectorViewSet

router = DefaultRouter()
router.register("free-dog-api", FreeDogAPIConnectorViewSet, basename="free-dog-api-connector")

urlpatterns = [
    path("", include(router.urls)),
]
