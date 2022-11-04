from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

from .models import Championship
from championships.serializer import ChampionshipSerializer
from .models import Championship


class ChampionshipView(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    serializer_class = ChampionshipSerializer
    queryset = Championship.objects.all()

    def perform_create(self, serializer):
        serializer.save(teams=self.request.data["teams"])


class ChampionshipDetailView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    serializer_class = ChampionshipSerializer
    queryset = Championship.objects.all()

    lookup_url_kwarg = "championship_id"
