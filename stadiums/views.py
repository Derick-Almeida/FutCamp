from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from utils import SerializerByMethodMixin, IsAdmin
from .models import Stadium
from .serializers import StadiumSerializer, StadiumDetailSerializer


class StadiumView(SerializerByMethodMixin, generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdmin]

    queryset = Stadium.objects.all()
    serializer_map = {
        "GET": StadiumSerializer,
        "POST": StadiumDetailSerializer,
    }


class StadiumDetailView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdmin]

    serializer_class = StadiumDetailSerializer
    queryset = Stadium.objects.all()

    lookup_url_kwarg = "stadium_id"
