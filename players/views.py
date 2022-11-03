from rest_framework import generics

from players.models import Player
from players.serializers import PlayerSerializer, PlayerDetailSerializer

from rest_framework.authentication import TokenAuthentication
from utils.permissions import IsAdmin, IsAdminOrReadOnly, IsOwner
from utils import SerializerByMethodMixin


class PlayerView(SerializerByMethodMixin, generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminOrReadOnly]

    queryset = Player.objects.all()
    serializer_map = {
        "GET": PlayerSerializer,
        "POST": PlayerDetailSerializer,
    }


class PlayerDetailView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsOwner, IsAdmin]

    queryset = Player.objects.all()
    serializer_class = PlayerDetailSerializer

    lookup_url_kwarg = "player_id"
