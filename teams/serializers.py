from rest_framework import serializers

from .models import Team
from players.serializers import PlayerSerializer


class TeamSerializer(serializers.ModelSerializer):
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
            "players",
            "coach",
            "stadium",
        )

    def get_number_of_players(self, obj: Team) -> int:
        return obj.players.all().count()
