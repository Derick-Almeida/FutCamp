from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from .models import Championship
from championships.serializer import ChampionshipSerializer


class ChampionshipView(generics.ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = ChampionshipSerializer
    queryset = Championship


class ChampionshipDetailView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = ChampionshipSerializer
    queryset = Championship

    lookup_url_kwarg = "championships_id"
