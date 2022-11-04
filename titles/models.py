from django.db import models
import uuid

class Title(models.Model):
       id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
       name = models.CharField(max_length=255)
       year_of_conquest = models.DateField()
       players = models.ForeignKey("players.Player",
       on_delete = models.CASCADE,
       related_name = "players",
       null=True,
       blank=True,
       default=None)
       team_id = models.ForeignKey("teams.Team",
        on_delete=models.CASCADE,
        related_name="titles",
        null=True,
        blank=True,
        default=None)

       coach_id = models.ForeignKey("coachs.Coach",
        on_delete = models.CASCADE,
        null=True,
        blank=True,
        default=None
        )

