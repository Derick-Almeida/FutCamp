from django.db import models
import uuid


class Player(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    age = models.IntegerField()
    hometown = models.CharField(max_length=150)
    # number_of_titles = models.IntegerField()
    biography = models.TextField()
    number_of_goals = models.IntegerField()
    position = models.CharField(max_length=50)
    shirt_number = models.IntegerField()
    team = models.ForeignKey(
        "teams.Team",
        on_delete=models.CASCADE,
        related_name="players",
    )
