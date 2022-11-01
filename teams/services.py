from django.shortcuts import get_object_or_404

from coachs.models import Coach
from stadiums.models import Stadium


def validate_updated_fields(serializer):
    if serializer["coach_id"] and serializer["stadium_id"]:
        coach_id = serializer.pop("coach_id")
        stadium_id = serializer.pop("stadium_id")

        coach = get_object_or_404(Coach, id=coach_id)
        stadium = get_object_or_404(Stadium, id=stadium_id)

        return serializer.save(coach=coach, stadium=stadium)

    if serializer["coach_id"]:
        coach_id = serializer.pop("coach_id")
        coach = get_object_or_404(Coach, id=coach_id)

        return serializer.save(coach=coach)

    if serializer["stadium_id"]:
        stadium_id = serializer.pop("stadium_id")
        stadium = get_object_or_404(Stadium, id=stadium_id)

        return serializer.save(stadium=stadium)
