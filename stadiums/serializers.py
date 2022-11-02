from rest_framework import serializers

from .models import Stadium
from .utils import TeamSerializer


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
            "team_owner",
        ]


class StadiumDetailSerializer(serializers.ModelSerializer):
    team_owner = TeamSerializer(default=None)

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
