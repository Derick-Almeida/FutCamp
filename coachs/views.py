from rest_framework import generics

from .serializers import CoachSerializer
from .models import Coach


class CreateListCoachView(generics.ListCreateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class GetUpdateDeleteCoachView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CoachSerializer
    queryset = Coach.objects.all()

    lookup_url_kwarg = "coach_id"
