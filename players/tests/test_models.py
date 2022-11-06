from django.test import TestCase
from users.models import User
from players.models import Player
from teams.models import Team

from model_bakery import baker


class PlayerModelTest(TestCase):
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

        cls.team = [baker.make("teams.Team")],

        # import ipdb
        # ipdb.set_trace()
        cls.player_created = Player.objects.create(
            **cls.player,
            current_team=cls.team[0].__getitem__(0),
        )

    def test_name_max_length(self):
        max_length = self.player_created._meta.get_field("name").max_length

        self.assertEqual(max_length, 255)

    def test_hometown_max_length(self):
        max_length = self.player_created._meta.get_field("hometown").max_length

        self.assertEqual(max_length, 150)

    def test_position_max_length(self):
        max_length = self.player_created._meta.get_field("position").max_length

        # Verificar se existe verifacação de Choices
        choices = self.player_created._meta.get_field("position").choices
        print(choices)

        self.assertEqual(max_length, 50)

    def test_current_team_null_blank(self):
        nullable = self.player_created._meta.get_field("current_team").null
        blankable = self.player_created._meta.get_field("current_team").blank

        self.assertEqual(nullable, True)
        self.assertEqual(blankable, True)
