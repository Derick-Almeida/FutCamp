from rest_framework import serializers

from .models import Stadium
from teams.serializers import TeamSerializer

class StadiumSerializer(serializers.ModelSerializer):
    team_owner = TeamSerializer(read_only=True)
    number_of_teams = serializers.SerializerMethodField()

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

    def get_number_of_teams(self, obj: Stadium) -> int:
        return obj.team_owner.all().count()





