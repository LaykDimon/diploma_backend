# Create your views here.

from codecs import lookup_error
from analyzer_api.parser import parse
from .models import AnalyzeResult, UserText
from .serializers import BaseTextSerializer, ResultsSerializer, URLSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from pickle import GET
from rest_framework import generics, status
from rest_framework.response import Response
from .utils import get_analyze_results
import time

class TextAnalyzer (generics.GenericAPIView):
    serializer_class = BaseTextSerializer
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            resultData = { 
                'text_stats': get_analyze_results(serializer.data['input_text']) 
            }
            analyze_result = AnalyzeResult.collection.create(symbol_count=resultData['text_stats']['symbol_count'],
                                            symbol_count_without_punct=resultData['text_stats']['symbol_count_without_punct'],
                                            word_count=resultData['text_stats']['word_count'],
                                            lemmatized_word_count=resultData['text_stats']['lemmatized_word_count'],
                                            sentence_count=resultData['text_stats']['sentence_count'],
                                            water_content=resultData['text_stats']['water_content'],
                                            classic_nausea=resultData['text_stats']['classic_nausea'],
                                            academic_nausea=resultData['text_stats']['academic_nausea'])
            
            user_text = UserText.collection.create(user_id=serializer.data['user_id'], 
                                                    content=serializer.data['input_text'], analyzeResult=analyze_result.to_dict())

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

class GetResults(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, id):
        
        userText_list = []
        for userText in UserText.collection.filter(user_id = id).fetch():
            userText_list.append(userText.to_dict())
        
        return Response(userText_list)