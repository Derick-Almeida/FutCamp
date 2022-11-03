from django.db import models
import uuid


class Championship(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    initial_date = models.DateField()
    end_date = models.DateField()
    award = models.FloatField()
    teams = models.ForeignKey(
        "teams.Team", related_name="championship", on_delete=models.CASCADE
    )
    games = models.ForeignKey(
        "games.Game", related_name="championship", on_delete=models.CASCADE
    )
