from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from .serializers import TitleSerializer
from .models import Title


class TitleView(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = []

    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class TitleDetailView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = []

    serializer_class = TitleSerializer
    queryset = Title.objects.all()

    lookup_url_kwarg = "title_id"
