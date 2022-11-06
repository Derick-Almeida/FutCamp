from rest_framework import serializers
from django.shortcuts import get_object_or_404

from .models import Title
from teams.models import Team


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = (
            "id",
            "name",
            "year_of_conquest",
        )


class TitleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = (
            "id",
            "name",
            "year_of_conquest",
            "coach",
            "team",
            "players",
        )

    def create(self, validated_data: dict) -> Title:
        team_id = validated_data.pop("team")
        team = get_object_or_404(Team, id=team_id)
        title = Title.objects.create(**validated_data)

        team.titles.add(title)
        team.coach.titles.add(title)

        for player in team.players.all():
            player.titles.add(title)

        team.save()

        return title
