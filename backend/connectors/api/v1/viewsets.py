import os

import requests
from rest_framework import viewsets

# from rest_framework.decorators import action
# from rest_framework.response import Response


class BaseConnectorViewSet(viewsets.GenericViewSet):
    title = None
    base_url = None
    auth_type = None

    def basic_api_call(self, url, method, auth=None, data=None):
        response = requests.request(method, url, data=data, auth=auth)
        return response.json()

    def get_auth(self):
        if self.auth_type == "basic":
            USERNAME_ENV_KEY = f"{self._get_env_title}_USERNAME"
            PASSWORD_ENV_KEY = f"{self._get_env_title}_PASSWORD"

            if USERNAME_ENV_KEY in os.environ and PASSWORD_ENV_KEY in os.environ:
                return requests.auth.HTTPBasicAuth(
                    os.environ[USERNAME_ENV_KEY], os.environ[PASSWORD_ENV_KEY]
                )

    def _get_env_title(self):
        return self.title.upper().replace(" ", "_")

"""
{
    "info": {
        "title": "Spotify Integrations",
        "version": "1.0.0",
        "description": "We will use this integration for accessing Spotify data.",
    },
    "paths": {
        "/albums/": {
            "get": {
                "security": [{"bearer": []}],
                "responses": {
                    "200": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/spotifyintegrations_response_get_GetAlbums"
                                }
                            }
                        },
                        "description": "Request completed successfully",
                    }
                },
                "parameters": [
                    {
                        "in": "path",
                        "name": "album_id",
                        "schema": {"type": "string"},
                        "required": true,
                        "description": "album_id",
                    }
                ],
                "description": "Get Albums",
                "operationId": "spotifyintegrations_get_albums_read",
            }
        },
        "/artists/": {
            "get": {
                "security": [{"bearer": []}],
                "responses": {
                    "200": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/spotifyintegrations_response_get_GetArtist"
                                }
                            }
                        },
                        "description": "Request completed successfully",
                    }
                },
                "parameters": [
                    {
                        "in": "path",
                        "name": "artist_id",
                        "schema": {"type": "string"},
                        "required": true,
                        "description": "artist_id",
                    }
                ],
                "description": "Get Artist",
                "operationId": "spotifyintegrations_get_artists_read",
            }
        },
    },
    "openapi": "3.0.1",
    "servers": [{"url": "https://api.spotify.com/v1"}],
    "components": {
        "schemas": {
            "spotifyintegrations_response_get_GetAlbums": {
                "type": "object",
                "properties": {
                    "artists": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "number", "description": "id "},
                                "href": {"type": "string", "description": "href"},
                                "type": {"type": "number", "description": "type"},
                                "external_urls": {
                                    "type": "string",
                                    "description": "external_urls",
                                },
                            },
                        },
                        "description": "artists",
                    },
                    "album_group": {"type": "string", "description": "album_group"},
                    "available_markets": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "available_markets",
                    },
                },
            },
            "spotifyintegrations_response_get_GetArtist": {
                "type": "object",
                "properties": {
                    "id": {"type": "string", "description": "id "},
                    "href": {"type": "string", "description": "href"},
                    "name": {"type": "string", "description": "name"},
                    "followers": {
                        "type": "object",
                        "properties": {
                            "total": {"type": "number", "description": "total"}
                        },
                        "description": "followers",
                    },
                    "popularity": {"type": "string", "description": "popularity"},
                    "external_urls": {
                        "type": "object",
                        "properties": {
                            "spotify": {"type": "string", "description": "spotify"}
                        },
                        "description": "external_urls",
                    },
                },
            },
        },
        "securitySchemes": {
            "bearer": {
                "type": "http",
                "scheme": "bearer",
                "x-env-var": ["SPOTIFY_API_INTEGRATION_TOKEN"],
            }
        },
    },
}
"""

class SpotifyIntegrationsConnectorViewSet(BaseConnectorViewSet):
    title = "Spotify Integrations"
    base_url = "https://api.spotify.com/v1"
    auth_type = "bearer"

    """
    "/albums/": {
            "get": {
                "security": [{"bearer": []}],
                "responses": {
                    "200": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/spotifyintegrations_response_get_GetAlbums"
                                }
                            }
                        },
                        "description": "Request completed successfully",
                    }
                },
                "parameters": [
                    {
                        "in": "path",
                        "name": "album_id",
                        "schema": {"type": "string"},
                        "required": true,
                        "description": "album_id",
                    }
                ],
                "description": "Get Albums",
                "operationId": "spotifyintegrations_get_albums_read",
            }
        }
    """
    @action(detail=False, methods=["get"])
    def albums(self, request):
        auth = self.get_auth()
        return Response(
            self.basic_api_call(
                self.base_url + "/albums", "get", auth=auth
            )
        )
    """
    "/artists/": {
            "get": {
                "security": [{"bearer": []}],
                "responses": {
                    "200": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/spotifyintegrations_response_get_GetArtist"
                                }
                            }
                        },
                        "description": "Request completed successfully",
                    }
                },
                "parameters": [
                    {
                        "in": "path",
                        "name": "artist_id",
                        "schema": {"type": "string"},
                        "required": true,
                        "description": "artist_id",
                    }
                ],
                "description": "Get Artist",
                "operationId": "spotifyintegrations_get_artists_read",
            }
        }
    """
    @action(detail=False, methods=["get"])
    def artists(self, request):
        auth = self.get_auth()
        return Response(
            self.basic_api_call(
                self.base_url + "/artists", "get", auth=auth
            )
        )
    


class FreeDogAPIConnectorViewSet(BaseConnectorViewSet):
    title = "Free Dog API"
    base_url = "https://dog.ceo/api"
    auth_type = "basic"

    @action(detail=False, methods=["get"])
    def breeds_image_random(self, request):
        auth = self.get_auth()
        return Response(
            self.basic_api_call(
                self.base_url + "/breeds/image/random", "get", auth=auth
            )
        )
