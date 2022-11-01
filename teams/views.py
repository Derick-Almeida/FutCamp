from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

from utils import IsAdminOrReadOnly
from .services import validate_updated_fields

from .serializers import TeamSerializer
from stadiums.models import Stadium
from coachs.models import Coach
from .models import Team


class TeamView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    def perform_create(self, serializer):
        coach_id = serializer.pop("coach_id")
        stadium_id = serializer.pop("stadium_id")

        coach = get_object_or_404(Coach, id=coach_id)
        stadium = get_object_or_404(Stadium, id=stadium_id)

        serializer.save(coach=coach, stadium=stadium)


class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    lookup_url_kwarg = "team_id"

    def perform_update(self, serializer):
        validate_updated_fields(serializer)

        serializer.save()
