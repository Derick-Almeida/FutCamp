from rest_framework import serializers

from teams.models import Team
from stadiums.models import Stadium
from championships.models import Championship


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium

        fields = [
            "id",
            "name",
            "description",
            "capacity",
            "localizations",
            "area",
        ]


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team

        fields = (
            "id",
            "name",
            "coach",
            "stadium",
        )


class ChampionshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Championship

        fields = (
            "id",
            "name",
            "description",
            "initial_date",
            "end_date",
            "award",
        )
