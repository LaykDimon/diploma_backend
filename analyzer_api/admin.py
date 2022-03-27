from typing import Text
from django.contrib import admin
from .models import AnalyzeResult, User, UserText

# Register your models here.
admin.site.register(User)
admin.site.register(AnalyzeResult)
admin.site.register(UserText)