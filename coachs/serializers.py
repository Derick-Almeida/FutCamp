from rest_framework import serializers
from datetime import date

from .models import Coach
from .utils import TeamSerializer


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = (
            "id",
            "name",
            "birthdate",
            "number_of_titles",
            "hometown",
            "current_team",
        )


class CoachDetailSerializer(serializers.ModelSerializer):
    current_team = TeamSerializer(default=None)
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
            "current_team",
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
