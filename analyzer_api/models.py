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
    words_number = models.IntegerField()
    words_number_with_spaces = models.IntegerField()
    words_number_without_spaces = models.IntegerField()
    letters_amount = models.IntegerField()
    foreign_words_amount = models.IntegerField()
    punctuation_marks = models.IntegerField()
    classic_nausea = models.FloatField()
    academic_nausea = models.FloatField()
    water_percentage = models.FloatField()