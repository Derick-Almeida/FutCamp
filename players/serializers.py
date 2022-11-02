from rest_framework import serializers
from players.models import Player
from teams.models import Team

from datetime import date

# from teams.serializers import TeamSerializer


class PlayerSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    number_of_goals = serializers.IntegerField(min_value=0)
    # current_team = TeamSerializer()

    class Meta:
        model = Player
        fields = (
            "id",
            "name",
            "birthdate",
            "age",
            "hometown",
            "biography",
            "number_of_goals",
            "position",
            "shirt_number",
            "current_team",
        )
        # read_only_fields = [
        #     "id",
        # ]

    def get_age(self, obj: Player) -> int:
        current_date = date.today()
        player_birthdate = date.fromisoformat(obj.birthdate)

        age = (
            current_date.year
            - player_birthdate.year
            - (
                (current_date.month, current_date.day)
                < (player_birthdate.month, player_birthdate.day)
            )
        )

        return age
