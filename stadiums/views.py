from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser

from .models import Stadium
from .serializers import StadiumSerializer


class StadiumView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    pagination_class = PageNumberPagination


class StadiumDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer

    lookup_url_kwarg = "stadium_id"
