from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from cnp_toolkit.cnp_analysis.analyze_cnp import analyze_cnp
from cnp_toolkit.cnp_generation.generate_cnp import generate_cnp
from cnp_toolkit.exceptions import CNPError
from cnp_toolkit.checksum import generate_checksum

# Create your views here.

@api_view(["POST"])
def analyze_endpoint(request):
    cnp = request.data.get("cnp")

    if not cnp:
        return Response(
            {"error": "CNP is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        result = analyze_cnp(cnp)
    except CNPError as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )

    return Response(result.__dict__)


@api_view(["POST"])
def generate_endpoint(request):
    try:
        result = generate_cnp(**request.data)
    except CNPError as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )

    return Response({"cnp": result})

@api_view(["POST"])
def checksum_endpoint(request):
    try:
        result = generate_checksum(**request.data)
    except CNPError as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )

    return Response({"checksum": result})