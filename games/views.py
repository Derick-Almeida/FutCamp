from rest_framework import generics

from games.models import Game
from games.serializers import GameSerializer

from rest_framework.authentication import TokenAuthentication

from utils.permissions import IsAdmin, IsAdminOrReadOnly, IsOwner


class GameView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        stadium = self.request.data["stadium"]
        teams = self.request.data["teams"]
        championship = self.request.data["championship"]
        # import pdb

        # pdb.set_trace()

        serializer.save(stadium=stadium, teams=teams, championship=championship)


class GameDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminOrReadOnly]

    lookup_url_kwarg = "game_id"
