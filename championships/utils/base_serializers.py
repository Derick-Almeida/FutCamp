from rest_framework import serializers
from datetime import date

from coachs.models import Coach
from stadiums.models import Stadium
from teams.models import Team
from games.models import Game


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium

        fields = ["id", "name", "description", "localizations"]


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = (
            "id",
            "name",
            "number_of_titles",
            "hometown",
        )


class TeamSerializer(serializers.ModelSerializer):
    coach = CoachSerializer(read_only=True)
    stadium = StadiumSerializer(read_only=True)
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


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game

        fields = "__all__"
