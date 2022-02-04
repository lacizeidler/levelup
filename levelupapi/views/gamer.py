"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
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

class GamerSerializer(ModelSerializer):
    class Meta:
        model = Gamer
        fields = "__all__"
        depth = 1
