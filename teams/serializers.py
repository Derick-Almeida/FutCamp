from rest_framework import serializers

from .models import Team
from .utils import StadiumSerializer, CoachSerializer

# from players.serializers import PlayerSerializer


class TeamSerializer(serializers.ModelSerializer):
    # number_of_players = serializers.SerializerMethodField()

    class Meta:
        model = Team

        fields = (
            "id",
            "name",
            "mascot",
            # "number_of_players",
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
    # players = PlayerSerializer(many=True, read_only=True)
    # number_of_players = serializers.SerializerMethodField()

    class Meta:
        model = Team

        fields = (
            "id",
            "name",
            "mascot",
            # "number_of_players",
            "team_foundation_year",
            "updated_at",
            "stadium",
            "coach",
            # "players",
        )

    def get_number_of_players(self, obj: Team) -> int:
        return obj.players.all().count()
