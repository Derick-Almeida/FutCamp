import ipdb
from rest_framework import generics
from rest_framework.views import APIView, Response, Request, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from utils import IsAdmin, IsOwner
from users.utils.user_extra_serializers import (
    UserFavoriteSerializer,
    UserFavoriteDetailSerializer,
)
from users.models import User

from teams.models import Team
from players.models import Player
from championships.models import Championship


class UserFavoriteTeamView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin | IsOwner]

    serializer_class = UserFavoriteSerializer
    queryset = Team.objects

    lookup_url_kwarg = "user_id"

    def get_queryset(self):
        return self.queryset.filter(users__id=self.kwargs["user_id"])


class UserFavoritePlayerView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin | IsOwner]

    serializer_class = UserFavoriteSerializer
    queryset = Player.objects.all()

    lookup_url_kwarg = "user_id"

    def get_queryset(self):
        return self.queryset.filter(users__id=self.kwargs["user_id"])


class UserFavoriteChampionshipView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin | IsOwner]

    serializer_class = UserFavoriteSerializer
    queryset = Championship.objects.all()

    lookup_url_kwarg = "user_id"

    def get_queryset(self):
        return self.queryset.filter(users__id=self.kwargs["user_id"])


class UserFavoriteDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin | IsOwner]

    serializer_class = UserFavoriteDetailSerializer
    queryset = User.objects.all()

    lookup_url_kwarg = "user_id"

    def perform_update(self, serializer):
        teams = self.request.data.get("favorite_teams", False)
        players = self.request.data.get("favorite_players", False)
        championships = self.request.data.get("favorite_championships", False)

        if teams:
            serializer.save(teams=teams)
        if self.request.data["favorite_player"]:
            serializer.save(players=players)
        if self.request.data["favorite_championship"]:
            serializer.save(championships=championships)

        serializer.save()
