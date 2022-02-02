"""View module for handling requests about game types"""
from urllib import response
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer
from levelupapi.models import GameType


class GameTypeView(ViewSet):
    def list(self, request):
        game_types = GameType.objects.all()
        serializer = GameTypeSerializer(game_types, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        game_type = GameType.objects.get(pk=pk)
        serializer = GameTypeSerializer(game_type)
        return Response(serializer.data)

    def create(self, request):
        game_type = GameType.objects.create(
            label=request.data['label']
        )
        serializer = GameTypeSerializer(game_type)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        game_type = GameType.objects.get(pk=pk)
        game_type.label = request.data['label']
        game_type.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        game_type = GameType.get(pk=pk)
        game_type.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class GameTypeSerializer(ModelSerializer):
    class Meta:
        model = GameType
        fields = ('id', 'label')
        depth = 1
