from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

class GenreChoices(models.TextChoices):
    HOMEM = "Homem"
    MULHER = "Mulher"
    NÃO_BINARIE = "Não Binárie"
    OTHER = "Não informado"


class User(AbstractUser):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255, unique = True)
    password = models.CharField(max_length = 255)
    birth_date = models.DateField(null = False)
    is_superuser = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    genre = models.CharField(
        max_length = 50,
        choices = GenreChoices.choices,
        default = GenreChoices.OTHER)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True, null = True, blank = True)
    favorite_teams = models.ForeignKey(
        'teams.Team',
        on_delete = models.CASCADE,
        related_name = "Teams",
        null = True
    )
    favorite_players = models.ForeignKey(
        "players.Player",
        on_delete = models.CASCADE,
        related_name = "Players",
        null = True
    )
    favorite_championships = models.ForeignKey(
        "championships.Championship",
        on_delete = models.CASCADE,
        related_name = "Championships",
        null = True
    )
