from datetime import timedelta, datetime

import jwt
from django.conf import settings


def create_token(user_id: int) -> dict:
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        'user_id': user_id,
        'access_token': create_access_token(
            data={
                'user_id': user_id
            },
            expires_delta=access_token_expires
        ),
        'token_type': 'Token',
    }


def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)) -> dict:
    to_encode = data.copy()
    expires = datetime.utcnow() + expires_delta
    to_encode.update({'exp': expires, 'sub': 'access'})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt
