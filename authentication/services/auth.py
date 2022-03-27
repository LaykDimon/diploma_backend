import jwt
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.exceptions import RefreshTokenError


def move_refresh_token_to_blacklist(refresh_token):
    try:
        token = RefreshToken(refresh_token)
        token.blacklist()
    except jwt.exceptions.InvalidTokenError:
        raise RefreshTokenError