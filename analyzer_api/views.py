# Create your views here.

from analyzer_api.parser import parse
from .serializers import BaseTextSerializer, URLSerializer
from rest_framework import permissions
from pickle import GET
from rest_framework import generics, status
from rest_framework.response import Response
from .utils import get_analyze_results

class TextAnalyzer (generics.GenericAPIView):
    serializer_class = BaseTextSerializer
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            resultData = { 
                'text_stats': get_analyze_results(serializer.data['input_text']) 
            }
            return Response(resultData, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UrlParser (generics.GenericAPIView):
    serializer_class = URLSerializer
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            resultData = { 
                'content': parse(serializer.data['url']) 
            }
            return Response(resultData, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)