from django.test import TestCase

# from games.models import Game
# from stadiums.models import Stadium
# from teams.models import Team
# from championships.models import Championship

from model_bakery import baker


class GameModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.championship = baker.make("championships.Championship")

        cls.game = baker.make(
            "games.Game",
            championship=cls.championship,
        )

    def test_result_max_length(self):
        max_length = self.game._meta.get_field("result").max_length

        self.assertEqual(max_length, 150)
