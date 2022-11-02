from rest_framework import serializers

from .models import Stadium
from teams.serializers import TeamSerializer


class StadiumSerializer(serializers.ModelSerializer):
    team_owner = TeamSerializer(read_only=True)

    class Meta:
        model = Stadium

        fields = [
            "id",
            "name",
            "description",
            "capacity",
            "localizations",
            "area",
            "team_owner",
        ]
