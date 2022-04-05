from unittest.util import _MAX_LENGTH
from rest_framework import serializers

class BaseTextSerializer (serializers.Serializer):
    input_text = serializers.CharField(max_length = 30000)

class URLSerializer (serializers.Serializer):
    url = serializers.URLField(max_length = 255)