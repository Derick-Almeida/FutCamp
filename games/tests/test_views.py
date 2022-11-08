# from rest_framework.test import APITestCase

# from stadiums.models import Stadium
# from teams.models import Team
# from championships.models import Championship
# from users.models import User
# from games.models import Game

# from model_bakery import baker


# class GameViewsTest(APITestCase):
#     @classmethod
#     def setUpTestData(cls):

#         cls.stadium = baker.make("stadiums.Stadium")
#         cls.championship = baker.make("championships.Championship")
#         cls.team_home = baker.make("teams.Team")
#         cls.team_away = baker.make("teams.Team")

#         cls.game = {
#             "date": "2022-08-30 20:00:00",
#             "result": "2x1",
#             "round": 1,
#             "stadium": str(cls.stadium.id),
#             "championship": str(cls.championship.id),
#             "teams": [
#                 str(cls.team_home.id),
#                 str(cls.team_away.id),
#             ],
#         }

#         cls.superuser_data = {
#             "name": "Adamastor",
#             "email": "adamastor@mail.com",
#             "password": "123456",
#             "birthdate": "1999-09-09",
#             "genre": "Masculino",
#         }

#         cls.superuser = User.objects.create_superuser(**cls.superuser_data)

#     def test_create_game(self):

#         login_data = {
#             "email": self.superuser_data["email"],
#             "password": self.superuser_data["password"],
#         }
#         login = self.client.post("/api/login/", login_data)
#         self.client.credentials(HTTP_AUTHORIZATION="Token " + login.data["token"])

#         import pdb

#         pdb.set_trace()

#         response = self.client.post("/api/games/", self.game)

#         # response_keys = set(response.data.keys())

#         # print(response)
#         # print(response_keys)

#         self.assertEqual(response.status_code, 201)
#         # self.assertSetEqual(self.expected_keys, response_keys)
