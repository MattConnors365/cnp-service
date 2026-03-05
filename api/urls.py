from django.urls import path
from .views import api_root, analyze_endpoint, generate_endpoint, checksum_endpoint

urlpatterns = [
    path("", api_root),
    path("analyze/", analyze_endpoint),
    path("generate/", generate_endpoint),
    path("validate", checksum_endpoint)
]