from django.shortcuts import get_object_or_404

from coachs.models import Coach
from stadiums.models import Stadium


def validate_updated_fields(validate_data, serializer):
    list_keys = validate_data.keys()

    if "coach" and "stadium" in list_keys:
        coach_id = validate_data.pop("coach")
        stadium_id = validate_data.pop("stadium")

        coach = get_object_or_404(Coach, id=coach_id)
        stadium = get_object_or_404(Stadium, id=stadium_id)

        return serializer.save(coach=coach, stadium=stadium)

    if "coach" in list_keys:
        coach_id = validate_data.pop("coach")
        coach = get_object_or_404(Coach, id=coach_id)

        return serializer.save(coach=coach)

    if "stadium" in list_keys:
        stadium_id = validate_data.pop("stadium")
        stadium = get_object_or_404(Stadium, id=stadium_id)

        return serializer.save(stadium=stadium)

    return serializer.save()
