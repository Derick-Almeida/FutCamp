from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication

from utils import IsAdminOrReadOnly, SerializerByMethodMixin
from .serializers import TeamSerializer, TeamDetailSerializer
from .services import validate_updated_fields

from stadiums.models import Stadium
from coachs.models import Coach
from .models import Team


class TeamView(SerializerByMethodMixin, generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminOrReadOnly]

    queryset = Team.objects.all()
    serializer_map = {
        "GET": TeamSerializer,
        "POST": TeamDetailSerializer,
    }

    def perform_create(self, serializer):
        coach_id = self.request.data.get("coach", None)
        stadium_id = self.request.data.get("stadium", None)

        coach = get_object_or_404(Coach, id=coach_id)
        stadium = get_object_or_404(Stadium, id=stadium_id)

        serializer.save(coach=coach, stadium=stadium)


class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminOrReadOnly]

    serializer_class = TeamDetailSerializer
    queryset = Team.objects.all()

    lookup_url_kwarg = "team_id"

    def perform_update(self, serializer):
        validate_updated_fields(self.request.data, serializer)
