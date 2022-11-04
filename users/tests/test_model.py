from django.test import TestCase

from users.models import User
from teams.models import Team
from players.models import Player
from championships.models import Championship


class UserTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.team_cadastro = {}
        cls.players_cadastro = {}
        cls.championship_cadastro = {}
        cls.team_test = Team.objects.create(**cls.team_cadastro)
        cls.player_test = Player.objects.create(**cls.players_cadastro)
        cls.championship_test = Championship.objects.create(**cls.championship_cadastro)

        cls.user_cadastro = {
            "name": "Xuxa Meneguel",
            "email": "xuxa@mail.com",
            "password": "ilarilarie",
            "birth_date": "1964-10-10",
            "genre": "Não Informado",
            "favorite_teams": cls.team_test,
            "favorite_players": cls.player_test,
            "favorite_championships": cls.championship_test,
        }

        cls.user_xuxa = User.objects.create_user(**cls.user_cadastro)

    def test_atributs(self):
        name_max = self.user_xuxa._meta.get_field("name").max_length
        email_max = self.user_xuxa._meta.get_field("email").max_length
        name_unique = self.user_xuxa._meta.get_field("name").unique
        email_unique = self.user_xuxa._meta.get_field("email").unique

        self.assertEqual(name_max, 255)
        self.assertEqual(email_max, 255)
        self.assertEqual(name_unique, False)
        self.assertEqual(email_unique, True)

    def test_values_input(self):
        self.assertEqual(self.user_xuxa.username, self.user_cadastro["name"])
        self.assertEqual(self.user_xuxa.birth_date, self.user_cadastro["birth_date"])
