from rest_framework.test import APITestCase

from users.models import User
from teams.models import Team
from players.models import Player
from championships.models import Championship


class UserViewerTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.register_url = "/api/users/register/"

        cls.team_cadastro = {

        }

        cls.players_cadastro = {

        }

        cls.championship_cadastro = {

        }

        cls.team_test = Team.objects.create(**cls.team_cadastro)
        cls.player_test = Player.objects.create(**cls.players_cadastro)
        cls.championship_test = Championship.objects.create(**cls.championship_cadastro)

        cls.user_cadastro_correto = {
            "name": "Xuxa Meneguel",
            "email": "xuxa@mail.com",
            "password" : "ilarilarie",
            "birth_date": "1964-10-10",
            "genre" : "Não Informado",
            "favorite_teams" : cls.team_test,
            "favorite_players" : cls.player_test,
            "favorite_championships": cls.championship_test
        }

        cls.user_cadastro_errado = {
            "name": "Xuxa Meneguel",
            "email": "xuxa@mail.com",
            "birth_date": "1964-10-10",
            "genre" : "Não Informado",
            "favorite_teams" : cls.team_test,
            "favorite_players" : cls.player_test,
            "favorite_championships": cls.championship_test
        }

        
    
    def test_can_register_new_user(self):
        response = self.client.post(self.register_url, self.user_cadastro_correto)

        user_count = User.objects.count()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], self.user_cadastro_correto['name'])
        self.assertEqual(response.data['email'], self.user_cadastro_correto['email'])
        self.assertEqual(1, user_count)

    def test_cannot_register_new_user(self):
        response = self.client.post(self.register_url, self.user_cadastro_errado)

        self.assertEqual(response.status_code, 400)

    def test_password_is_hashed (self):
        response = self.client.post(self.register_url, self.user_cadastro_correto)
        user = User.objects.first()

        is_password_true = user.check_password(self.user_cadastro_correto['password'])

        self.assertTrue(is_password_true)
    
    def test_returning_keys (self):
        response = self.client.post(self.register_url, self.user_cadastro_correto)

        user_keys = {   
                "id",
                "name",
                "email",
                "birth_date", 
                "is_superuser", 
                "is_active", 
                "genre", 
                "created_at",
                "updated_at",
                "favorite_teams",
                "favorite_players",
                "favorite_championships" 
                    }
        
        response_keys = set(response.data.keys())

        self.assertSetEqual(user_keys, response_keys)