from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

from .models import Stadium
from .serializers import StadiumSerializer


class StadiumView(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    serializer_class = StadiumSerializer
    queryset = Stadium.objects.all()


class StadiumDetailView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    serializer_class = StadiumSerializer
    queryset = Stadium.objects.all()

    lookup_url_kwarg = "stadium_id"
