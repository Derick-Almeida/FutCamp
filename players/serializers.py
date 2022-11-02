from rest_framework import serializers
from players.models import Player
from teams.models import Team

# from teams.serializers import TeamSerializer


class PlayerSerializer(serializers.ModelSerializer):
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
