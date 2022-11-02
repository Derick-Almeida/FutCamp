from rest_framework import serializers
from datetime import date

from teams.serializers import TeamSerializer
from .models import Coach


class CoachSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    current_team = TeamSerializer(read_only=True)

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
