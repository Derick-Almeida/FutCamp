from django.test import TestCase
from users.models import User
from .models import Championship


class Test_Championship(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.admin_obj = {}
        cls.admin_data = User.objects.create_superuser(**cls.admin_obj)

    def test_create_championship_and_possibles_errors(self):

        championships_obj = {}
        championships_data = Championship.objects.create(**championships_obj)

        championships_obj_error = {}
        championships_obj_error_data = Championship.objects.create(
            **championships_obj_error
        )

        result_status_error = championships_obj_error_data.status_code
        expected_status_error = 400

        result_status = championships_data.status_code
        expected_status = 201

        self.assertEqual(result_status_error, expected_status_error)
        self.assertEqual(result_status, expected_status)
