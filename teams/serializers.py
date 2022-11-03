from rest_framework import serializers
from django.shortcuts import get_object_or_404

from .models import Team
from players.models import Player
from .utils import StadiumSerializer, CoachSerializer, PlayerSerializer


class TeamSerializer(serializers.ModelSerializer):
    number_of_players = serializers.SerializerMethodField()

    class Meta:
        model = Team

        fields = (
            "id",
            "name",
            "mascot",
            "number_of_players",
            "team_foundation_year",
            "updated_at",
            "stadium",
            "coach",
        )

    def get_number_of_players(self, obj: Team) -> int:
        return obj.players.all().count()


class TeamDetailSerializer(serializers.ModelSerializer):
    coach = CoachSerializer(read_only=True)
    stadium = StadiumSerializer(read_only=True)
    players = PlayerSerializer(many=True, read_only=True)
    number_of_players = serializers.SerializerMethodField()

    class Meta:
        model = Team

        fields = (
            "id",
            "name",
            "mascot",
            "number_of_players",
            "team_foundation_year",
            "updated_at",
            "stadium",
            "coach",
            "players",
        )

    def get_number_of_players(self, obj: Team) -> int:
        return obj.players.all().count()

    def create(self, validated_data):
        list_keys = validated_data.keys()
        player_list = []

        if "players" in list_keys:
            players = validated_data.pop("players")

            for player_id in players:
                player = get_object_or_404(Player, id=player_id)
                player_list.append(player)

        team = Team.objects.create(**validated_data)
        team.players.set(player_list)

        return team
