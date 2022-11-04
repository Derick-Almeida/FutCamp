from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Championship

from .utils import TeamSerializer, GameSerializer
from teams.models import Team


class ChampionshipSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True, read_only=True)
    games = GameSerializer(many=True, read_only=True)

    class Meta:
        model = Championship

        fields = (
            "id",
            "name",
            "description",
            "initial_date",
            "end_date",
            "award",
            "teams",
            "games",
        )

    def create(self, validated_data: dict) -> Championship:
        team_list = validated_data.pop("teams")
        teams = []

        for team_id in team_list:
            team = get_object_or_404(Team, id=team_id)
            teams.append(team)

        championship = Championship.objects.create(**validated_data)
        championship.teams.set(teams)

        return championship
