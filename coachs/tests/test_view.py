from rest_framework.test import APITestCase
from coachs.models import Coach


class CoachViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.coach_data = {
            "name": "teste",
            "birth_date": "2000-08-15",
            "age": 22,
            "biography": "ajkfasklfklas",
            "number_of_titles": 5,
            "hometown": "recife",
            "current_team": "barcelona",
        }

        cls.coach = Coach.objects.create(**cls.coach_data)

    def test_create_coach(self):
        coach_response = self.client.post("/api/coach/", self.coach_data)
        self.assertEqual(coach_response.status_code, 201)
        self.assertEqual(coach_response.data["name"], "teste")
        self.assertEqual(coach_response.data["number_of_titles"], 5)

    def test_get_coachs(self):
        response = self.client.get("/api/coach/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 1)

    def test_get_coach(self):
        coach_response = self.client.post("/api/coach/", self.coach_data)
        coach_id = coach_response.data["id"]
        coach = self.client.get(f"/api/coach/{coach_id}/")
        self.assertEqual(coach.status_code, 200)
        self.assertEqual(coach.data["results"][0]["name"], "teste")

    def test_update_coachs(self):
        coach_response = self.client.post("/api/coach/", self.coach_data)
        coach_id = coach_response.data["id"]
        coach_update = self.client.patch(
            f"/api/coach/{coach_id}/", {"name": "update-coach"}
        )
        self.assertEqual(coach_update.status_code, 200)
        self.assertEqual(coach_update.data["name"], "update-coach")

    def test_delete_coach(self):
        coach_response = self.client.post("/api/coach/", self.coach_data)
        coach_id = coach_response.data["id"]
        coach_delete = self.client.delete(f"/api/coach/{coach_id}/")
        self.assertEqual(coach_delete.status_code, 204)
