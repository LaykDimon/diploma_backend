from fireo import models
from authentication.models import User

# Create your models here.
class Trackable(models.Model):
    created_at = models.DateTime(auto=True)
    updated_at = models.DateTime(auto=True)

    class Meta:
        abstract = True

class AnalyzeResult(models.Model):
    symbol_count = models.NumberField(int_only=True)
    symbol_count_without_punct = models.NumberField(int_only=True)
    word_count = models.NumberField(int_only=True)
    lemmatized_word_count = models.NumberField(int_only=True)
    sentence_count = models.NumberField(int_only=True)
    water_content = models.NumberField(float_only=True)
    classic_nausea = models.NumberField(float_only=True)
    academic_nausea = models.NumberField(float_only=True)


class UserText(Trackable):
    user_id = models.NumberField(int_only=True)
    content = models.TextField()
    analyzeResult = models.MapField()


