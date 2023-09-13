from rest_framework import viewsets, mixins


class BaseConnectorViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    ...


class SSpotifyConnectorViewSet(BaseConnectorViewSet):
    ...
