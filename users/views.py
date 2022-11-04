from rest_framework import generics

from .models import User
from .serializers import UserSerializer, UserDetailSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserListView(generics.ListAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = []

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = []

    serializer_class = UserDetailSerializer
    queryset = User.objects.all()

    lookup_url_kwarg = "user_id"


class EnableDisableUserView(generics.UpdateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = []

    serializer_class = UserDetailSerializer
    queryset = User.objects.all()

    lookup_url_kwarg = "user_id"
