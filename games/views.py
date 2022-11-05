from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from .models import Game
from .serializers import GameSerializer, GameDetailSerializer
from utils import IsAdminOrReadOnly, SerializerByMethodMixin


class GameView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Game.objects.all()
    serializer_map = {
        "GET": GameSerializer,
        "POST": GameDetailSerializer,
    }

    def perform_create(self, serializer):
        stadium = self.request.data["stadium"]
        teams = self.request.data["teams"]
        championship = self.request.data["championship"]

        serializer.save(stadium=stadium, teams=teams, championship=championship)


class GameDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Game.objects.all()
    serializer_class = GameSerializer

    lookup_url_kwarg = "game_id"
