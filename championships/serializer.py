from rest_framework import serializers
from .models import Championship


class ChampionshipSerializer(serializers.ModelSerializer):
    class Meta:
        model: Championship
        fields = (
            "id",
            "name",
            "description",
            "initial_date",
            "end_date",
            "award",
            "teams",
            "games",
        )
        # read_only_fields = ["initial_date", "end_date"]
