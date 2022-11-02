import uuid

from django.db import models


class Stadium(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    capacity = models.PositiveIntegerField()
    localizations = models.CharField(max_length=255)
    area = models.FloatField()

    team_owner = models.OneToOneField(
        "teams.Team", on_delete=models.CASCADE, related_name="stadiums"
    )
