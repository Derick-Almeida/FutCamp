from django.shortcuts import get_object_or_404

from coachs.models import Coach
from stadiums.models import Stadium
from players.models import Player


def validate_team_fields(validated_data, serializer):
    list_keys = validated_data.keys()

    if "coach" and "stadium" in list_keys:
        coach_id = validated_data.pop("coach")
        stadium_id = validated_data.pop("stadium")

        coach = get_object_or_404(Coach, id=coach_id)
        stadium = get_object_or_404(Stadium, id=stadium_id)

        if "players" in list_keys:
            player_list = validated_data.pop("players")
            return serializer.save(coach=coach, stadium=stadium, players=player_list)

        return serializer.save(coach=coach, stadium=stadium)

    if "coach" in list_keys:
        coach_id = validated_data.pop("coach")
        coach = get_object_or_404(Coach, id=coach_id)

        if "players" in list_keys:
            player_list = validated_data.pop("players")
            return serializer.save(coach=coach, players=player_list)

        return serializer.save(coach=coach)

    if "stadium" in list_keys:
        stadium_id = validated_data.pop("stadium")
        stadium = get_object_or_404(Stadium, id=stadium_id)

        if "players" in list_keys:
            player_list = validated_data.pop("players")
            return serializer.save(stadium=stadium, players=player_list)

        return serializer.save(stadium=stadium)

    if "players" in list_keys:
        player_list = validated_data.pop("players")
        return serializer.save(players=player_list)

    return serializer.save()
