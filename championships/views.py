from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from .models import Championship
from championships.serializer import ChampionshipSerializer
from django.shortcuts import get_list_or_404, get_object_or_404
from teams.models import Team
from games.models import Game
from .models import Championship


class ChampionshipView(generics.ListCreateAPIView):

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    serializer_class = ChampionshipSerializer
    queryset = Championship.objects.all()


class ChampionshipDetailView(generics.RetrieveUpdateDestroyAPIView):

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    serializer_class = ChampionshipSerializer
    queryset = Championship.objects.all()

    lookup_url_kwarg = "championships_id"

    def perform_create(self, serializer):
        serializer.save(championships_id=self.kwargs["championships_id"])
