from unittest.util import _MAX_LENGTH
from rest_framework import serializers

class BaseTextSerializer (serializers.Serializer):
    input_text = serializers.CharField(max_length = 30000)

class URLSerializer (serializers.Serializer):
    url = serializers.URLField(max_length = 255)

class AnalyzeResultSerializer(serializers.Serializer):
    symbol_count = serializers.IntegerField()
    symbol_count_without_punct = serializers.IntegerField()
    word_count = serializers.IntegerField()
    lemmatized_word_count = serializers.IntegerField()
    sentence_count = serializers.IntegerField()
    water_content = serializers.FloatField()
    classic_nausea = serializers.FloatField()
    academic_nausea = serializers.FloatField()