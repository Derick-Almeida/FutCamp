from rest_framework import serializers
from datetime import date

from teams.models import Team
from coachs.models import Coach
from stadiums.models import Stadium


class CoachSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = Coach
        fields = (
            "id",
            "name",
            "birthdate",
            "age",
            "biography",
            "number_of_titles",
            "hometown",
        )

    def get_age(self, obj: Coach) -> int:
        current_date = date.today()
        coach_birthdate = obj.birthdate

        age = (
            current_date.year
            - coach_birthdate.year
            - (
                (current_date.month, current_date.day)
                < (coach_birthdate.month, coach_birthdate.day)
            )
        )

        return age


class TeamSerializer(serializers.ModelSerializer):
    coach = CoachSerializer(read_only=True)
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
            "coach",
            # "players",
        )

    def get_number_of_players(self, obj: Team) -> int:
        return obj.players.all().count()
