from django.urls import path
from .views import analyze_endpoint, generate_endpoint, checksum_endpoint

urlpatterns = [
    path("analyze/", analyze_endpoint),
    path("generate/", generate_endpoint),
    path("validate", checksum_endpoint)
]