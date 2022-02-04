from levelupapi.models.event import Event
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.serializers import ModelSerializer
from levelupapi.models.game import Game
from rest_framework import status
from levelupapi.models.gamer import Gamer


class EventView(ViewSet):
    def list(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def create(self, request):
        organizer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data['game'])

        event = Event.objects.create(
            description=request.data['description'],
            data=request.data['date'],
            time=request.data['time'],
            organizer=organizer,
            game=game
        )
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        depth = 1
