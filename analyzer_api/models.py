from django.db import models
from authentication.models import User

# Create your models here.
class Trackable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserText(Trackable):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    analyzeResult = models.ForeignKey('AnalyzeResult', on_delete=models.CASCADE)

class AnalyzeResult(models.Model):
    symbol_count = models.IntegerField()
    symbol_count_without_punct = models.IntegerField()
    word_count = models.IntegerField()
    sentence_count = models.IntegerField()
    water_content = models.FloatField()
    classic_nausea = models.FloatField()
    academic_nausea = models.FloatField()