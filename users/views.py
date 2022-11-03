from rest_framework import generics
from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404

from .models import User

from .serializers import UserSerializer

class UserCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects

class UserIDView(APIView):
    def get (self, request: Request, user_id: str) -> Response:

        user_by_id = get_object_or_404(User, id = user_id)

        serializer = UserSerializer(user_by_id)

        return Response(serializer.data, status.HTTP_200_OK)
    
    def patch (self, request: Request, user_id: str) -> Response:

        user_by_id = get_object_or_404(User, id = user_id)

        for key, value in request.data.items():
            setattr(user_by_id, key, value)
        
        user_by_id.save()

        serializer = UserSerializer(user_by_id)

        return Response(serializer.data, status.HTTP_200_OK)

