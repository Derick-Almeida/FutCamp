from rest_framework import generics
from .models import User
from .serializers import UserSerializer, UserDetailSerializer
from .serializers import Loginserializer
from rest_framework.views import APIView, Response, Request, status
from django.contrib.auth import authenticate

# from users.utils import email_verificate

from django.shortcuts import get_object_or_404
from .models import User
from rest_framework.views import APIView, Response, status
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token


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


class loginView(APIView):
    def post(self, request: Request):
        serializer = Loginserializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data.get("email"),
            password=serializer.validated_data.get("password"),
        )
        username = (serializer.validated_data.get("email"),)
        password = (serializer.validated_data.get("password"),)
        print(user)
        print("=" * 100)
        print(username)
        print("=" * 100)
        print(password)

        if not user:
            return Response(
                {"detail": "invalid credentials"}, status.HTTP_403_FORBIDDEN
            )
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
