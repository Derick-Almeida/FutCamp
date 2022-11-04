from django.shortcuts import get_object_or_404
from ..models import User
from rest_framework.views import APIView, Response, status
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token


class email_verificate(APIView):
    def verificate_hash(self, password=None):
        hashers_password = make_password(password)
        _ = get_object_or_404(User, password=hashers_password)
        return _

    def verificate_email(self, email):
        _ = get_object_or_404(User, email=email, )
        return _

    def verificate_user(self, email, password=None):
        if not self.verificate_email(email) or not self.verificate_hash(password):
            return Response(
                {"detail": "invalid credentials"}, status.HTTP_403_FORBIDDEN
            )
        token, _ = Token.objects.get_or_create(email=email)
        return Response({"token": token.key})
