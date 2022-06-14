from django.urls import path
from analyzer_api import views
from .views import TextAnalyzer, UrlParser, GetResults


urlpatterns = [
    path('analyzer/', TextAnalyzer.as_view(), name = 'Analyzer' ),
    path('analyzer/parse/', UrlParser.as_view(), name = 'Parser'),
    path('analyzer/results/<int:id>', GetResults.as_view(), name = 'Results')
]