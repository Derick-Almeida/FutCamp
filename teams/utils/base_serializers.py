from rest_framework import serializers
from datetime import date

from titles.models import Title
from coachs.models import Coach
from players.models import Player
from stadiums.models import Stadium


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
            "number_of_titles",
            "hometown",
            "current_team",
        )

    def get_number_of_titles(self, obj: Coach) -> int:
        return obj.titles.all().count()

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


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = (
            "id",
            "name",
            "year_of_conquest",
        )
