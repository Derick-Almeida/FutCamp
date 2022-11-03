from rest_framework import serializers
from players.models import Player
from teams.models import Team

from datetime import date

from .utils import TeamSerializer


class PlayerSerializer(serializers.ModelSerializer):
    number_of_goals = serializers.IntegerField(min_value=0)

    class Meta:
        model = Player
        fields = (
            "id",
            "name",
            "birthdate",
            "hometown",
            "number_of_goals",
            "position",
            "shirt_number",
            "current_team",
        )


class PlayerDetailSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    number_of_goals = serializers.IntegerField(min_value=0)
    current_team = TeamSerializer()

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

    def get_age(self, obj: Player) -> int:
        current_date = date.today()
        player_birthdate = obj.birthdate

        age = (
            current_date.year
            - player_birthdate.year
            - (
                (current_date.month, current_date.day)
                < (player_birthdate.month, player_birthdate.day)
            )
        )

        return age

    # def validate_number_of_goals(self, value):
    #     if value < 0:
    #         raise serializers.ValidationError(
    #             "number of goals must be greater than zero"
    #         )

    #     return value
