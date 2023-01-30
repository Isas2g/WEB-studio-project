from django.shortcuts import render
from loguru import logger
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from ..serializers import GoogleAuthSerializer
from ..services.google_auth import google_auth


def google_login(request):
    return render(request, 'oauth/google_login.html')


@api_view(["POST"])
def google_auth_(request):
    google_data = GoogleAuthSerializer(data=request.data)
    if google_data.is_valid():
        token = google_auth(google_data.data)
        return Response(token)
    else:
        return AuthenticationFailed(code=403, detail='Bad data Google')