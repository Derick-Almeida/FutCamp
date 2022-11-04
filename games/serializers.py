from rest_framework import serializers
from games.models import Game

from .utils import (
    StadiumSerializer,
    PlayerSerializer,
    CoachSerializer,
    TeamSerializer,
    ChampionshipSerializer,
)

from stadiums.models import Stadium
from teams.models import Team
from championships.models import Championship

from django.shortcuts import get_object_or_404


class GameSerializer(serializers.ModelSerializer):
    stadium = StadiumSerializer(read_only=True)
    teams = TeamSerializer(many=True, read_only=True)
    championship = ChampionshipSerializer(read_only=True)

    class Meta:
        model = Game
        fields = (
            "id",
            "date",
            "result",
            "stadium",
            "teams",
            "championship",
        )
        read_only_fields = [
            "stadium",
            "teams",
            "championship",
        ]

    def create(self, validated_data):
        stadium_id = validated_data.pop("stadium")
        teams_id = validated_data.pop("teams")
        championship_id = validated_data.pop("championship")
        teams = []

        for team_id in teams_id:
            team = get_object_or_404(Team, id=team_id)
            teams.append(team)

        stadium = get_object_or_404(Stadium, id=stadium_id)
        championship = get_object_or_404(Championship, id=championship_id)

        game = Game.objects.create(
            **validated_data,
            stadium=stadium,
            championship=championship,
        )
        game.teams.set(teams)

        return game
