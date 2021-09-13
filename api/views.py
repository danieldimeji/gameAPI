from django.shortcuts import get_object_or_404

from .models import *
from .serializers import GameSerializer

from scraper import selenium_script
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status




class GamesViewSet(viewsets.ViewSet):

    # GET REQUEST TO ROOT URL
    def list(self, request):
        games = Games.objects.all()
        serializers = GameSerializer(games, many=True)
        return Response(serializers.data) 
    
    # POST REQUEST TO ROOT URL
    def create(self, request):
        serializers = GameSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

    # GET REQUEST TO ROOT URL/ ID OR PRIMARY KEY
    def retrieve(self, request, pk=None):
        querySet = Games.objects.all()
        games = get_object_or_404(querySet, pk=pk)
        serializers = GameSerializer(games)
        return Response(serializers.data)


    # PUT REQUEST TO ROOT URL/ ID OR PRIMARY KEY
    def update(self, request, pk=None):
        games = Games.objects.get(pk=pk)
        serializers = GameSerializer(games,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    # DELETE REQUEST TO ROOT URL/ ID OR PRIMARY KEY
    def destroy(self, request, pk=None):
        games = self.get_object(id)
        games.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
