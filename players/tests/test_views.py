from rest_framework.test import APITestCase

from users.models import User
from players.models import Player
from teams.models import Team

from model_bakery import baker


class PlayerViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):

        cls.player = {
            "name": "Gabriel Barbosa",
            "birthdate": "1996-10-14",
            "hometown": "Santos-SP",
            "biography": "Decidiu duas libertadores para o Flamengo",
            "number_of_goals": 200,
            "position": "Atacante",
            "shirt_number": 10,
        }

        cls.team = {
            baker.make("teams.Team"),
        }
        # import ipdb
        # ipdb.set_trace()
        cls.player_created = Player.objects.create(
            **cls.player,
            current_team=cls.team.id,
        )

        ...
