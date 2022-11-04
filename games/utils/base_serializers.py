from rest_framework import serializers
from datetime import date

from teams.models import Team
from coachs.models import Coach
from players.models import Player
from stadiums.models import Stadium
from championships.models import Championship


class CoachSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    number_of_titles = serializers.SerializerMethodField()

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

    def get_number_of_titles(self, obj: Coach) -> int:
        return obj.titles.all().count()


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
        )


class TeamSerializer(serializers.ModelSerializer):
    coach = CoachSerializer(read_only=True)
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
            "coach",
            "players",
        )

    def get_number_of_players(self, obj: Team) -> int:
        return obj.players.all().count()


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
