from rest_framework.exceptions import APIException
from rest_framework import status


class RefreshTokenError(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'Refresh token expired or invalid'