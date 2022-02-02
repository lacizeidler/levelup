"""View module for handling requests about game types"""
from urllib import response
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer
from levelupapi.models.gamer import Gamer


class GamerView(ViewSet):
    def list(self, request):
        gamer = Gamer.objects.all()
        serializer = GamerSerializer(gamer, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        gamer = Gamer.objects.get(pk=pk)
        serializer = GamerSerializer(gamer)
        return Response(serializer.data)

    def create(self, request):
        gamer = Gamer.objects.create(
            label=request.data['label']
        )
        serializer = GamerSerializer(gamer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        gamer = Gamer.objects.get(pk=pk)
        gamer.label = request.data['bio']
        gamer.user_id = request.data['user_id']
        gamer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        gamer = Gamer.get(pk=pk)
        gamer.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class GamerSerializer(ModelSerializer):
    class Meta:
        model = Gamer
        fields = ('id', 'bio', 'user_id')
        depth = 1
