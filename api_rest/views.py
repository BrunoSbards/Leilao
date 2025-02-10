from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import leiloeiro
from .serializers import leiloeiroSerializer

import json

@api_view(['GET'])
def get_leiloeiro(request):

    if request.method == 'GET':

        nome = leiloeiro.objects.all()                          

        serializer = leiloeiroSerializer(leiloeiro, many=True)       

        return Response(serializer.data)                    
    
    return Response(status=status.HTTP_400_BAD_REQUEST)