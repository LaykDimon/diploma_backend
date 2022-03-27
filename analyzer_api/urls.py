from django.urls import path
from .views import TextAnalyzer, UrlParser

urlpatterns = [
    path('analyzer/', TextAnalyzer.as_view(), name = 'Analyzer' ),
    path('analyzer/parse/', UrlParser.as_view(), name = 'Parser'),
]