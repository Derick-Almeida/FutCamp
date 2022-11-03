from django.test import TestCase
from users.models import User
from .models import Championship


class Test_Championship(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        # URLS

        cls.URL_create_championship = "api/championships/"
        cls.URL_login = "api/login/"

        # OBJS

        cls.admin_obj = {
            "username": "gabriel",
            "email": "ggabriel.p2003@gmail.com",
            "password": "1234",
        }

        cls.admin_data = User.objects.create_superuser(**cls.admin_obj)

    def test_create_championship(self):

        superUser = {
            "username": "gabriel",
            "password": "1234"
        }

        token = self.client.post(self.URL_login, superUser)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.data["token"])

        championships_obj = {
            "name": "c",
            "description": "description",
            "initial_date": "01-01-2003",
            "end_date": "end_date",
            "award": "9,2",
            "teams": "1",
            "games": "2",
        }

        championships_data = self.client.post(**championships_obj)

        result_status = championships_data.status_code
        expected_status = 201

        self.assertEqual(result_status, expected_status)

    def test_possibles_errors_the_championship(self):

        superUser = {
            "username": "gabriel",
            "password": "1234"
        }

        token = self.client.post(self.URL_login, superUser)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.data["token"])

        championships_obj_error = {}

        championships_obj_error_data = Championship.objects.create(
            **championships_obj_error
        )

        result_status_error = championships_obj_error_data.status_code
        expected_status_error = 400

        self.assertEqual(result_status_error, expected_status_error)
