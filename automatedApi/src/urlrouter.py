from rest_framework import generics
from django.http.response import JsonResponse
from src.urlrouterlib import URLRouterLib

class URLRouterView(generics.GenericAPIView):
    def get(self, request):
        return JsonResponse(
            URLRouterLib(request).get_requests
        )

