from rest_framework import generics

from utils import SerializerByMethodMixin, IsAdminOrReadOnly
from .serializers import CoachSerializer, CoachDetailSerializer
from .models import Coach


class CreateListCoachView(SerializerByMethodMixin, generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminOrReadOnly]

    queryset = Coach.objects.all()
    serializer_map = {
        "GET": CoachSerializer,
        "POST": CoachDetailSerializer,
    }


class GetUpdateDeleteCoachView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminOrReadOnly]

    serializer_class = CoachDetailSerializer
    queryset = Coach.objects.all()

    lookup_url_kwarg = "coach_id"
