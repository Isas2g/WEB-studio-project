from google.oauth2 import id_token
from google.auth.transport import requests
from loguru import logger
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from src.users.models import User
from src.users.serializers import GoogleAuthSerializer
from .base_auth import create_token


def google_auth(google_user: GoogleAuthSerializer) -> dict:
    try:
        id_token.verify_oauth2_token(google_user['token'],
                                     requests.Request(),
                                     settings.GOOGLE_CLIENT_ID)
    except ValueError:
        raise AuthenticationFailed(code=403, detail='Bad token Google')

    user, _ = User.objects.get_or_create(email=google_user['email'])
    return create_token(user.id)
