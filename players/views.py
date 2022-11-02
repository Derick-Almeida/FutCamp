from rest_framework import generics

from players.models import Player
from players.serializers import PlayerSerializer

from rest_framework.authentication import TokenAuthentication
from utils.permissions import IsAdmin, IsAdminOrReadOnly, IsOwner


class PlayerView(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]


class PlayerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwner, IsAdmin]

    lookup_url_kwarg = "player_id"
