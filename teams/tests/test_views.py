from rest_framework.test import APITestCase
from rest_framework.views import status

from model_bakery import baker


class SongViewTests(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.coach = baker.make("coachs.Coach")
        cls.stadium = baker.make("stadiums.Stadium")
        cls.players = [baker.make("players.Player") for _ in range(5)]
        cls.team_data = {
            "name": "Bigode Grosso FC",
            "mascot": "El bigodon",
            "team_foundation_year": "1993-09-09",
            "coach": cls.coach,
            "stadium": cls.stadium,
            "players": cls.players,
        }

        cls.expected_keys = {
            "id",
            "name",
            "number_of_players",
            "mascot",
            "team_foundation_year",
            "updated_at",
            "players",
            "coach",
            "stadium",
        }

    def test_create_team_empty_body(self):
        """Não deve ser capaz de criar um novo `team` caso o corpo da requisição esteja vazio"""

        response = self.client.post(self.BASE_URL, {})

        expected_status = status.HTTP_400_BAD_REQUEST
        expected_keys = {
            "name",
            "mascot",
            "team_foundation_year",
            "players",
            "coach",
            "stadium",
        }

        result_status = response.status_code
        result_keys = set(response.data.keys())

        msg_status = "O status code recebido esta diferente do esperado"

        self.assertEqual(expected_status, result_status, msg_status)
        self.assertSetEqual(expected_keys, result_keys)

    def test_create_team(self):
        """Deve ser capaz de criar um novo `team`"""

        response = self.client.post("/api/teams/", self.team_data)

        expected_status = status.HTTP_201_CREATED

        result_status = response.status_code
        result_keys = set(response.data.keys())

        msg_status = "O status code recebido esta diferente do esperado"

        self.assertEqual(expected_status, result_status, msg_status)
        self.assertSetEqual(self.expected_keys, result_keys)
