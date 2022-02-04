"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer
from levelupapi.models import Game
from levelupapi.models.game_type import GameType
from levelupapi.models.gamer import Gamer


class GameView(ViewSet):
    def list(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def create(self, request):
        gamer = Gamer.objects.get(user=request.auth.user)
        game_type = GameType.objects.get(pk=request.data['game_type_id'])

        game = Game.objects.create(
            title=request.data['title'],
            maker=request.data['maker'],
            number_of_players=request.data['number_of_players'],
            skill_level=request.data['skill_level'],
            game_type=game_type,
            gamer=gamer
        )
        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        game = Game.objects.get(pk=pk)
        game.title = request.data['title']
        game.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        game = Game.objects.get(pk=pk)
        game.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"
        depth = 1
