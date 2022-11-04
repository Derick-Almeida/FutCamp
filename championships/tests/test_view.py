from rest_framework.test import APITestCase
from championships.models import Championship


class ChampionshipsViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.championship_data = {
            "name": "garcia",
            "description": "awsgfasdverfw dffwg ffegfegdh",
            "initial_date": "2002-03-04",
            "end_date": "2003-03-04",
            "award": "9.2",
        }

        cls.championship = Championship.objects.create(**cls.championship_data)

    def test_create_championship(self):
        championship_response = self.client.post(
            "/api/championships/", self.championship_data
        )
        self.assertEqual(championship_response.status_code, 201)
        self.assertEqual(championship_response.data["award"], 9.2)
        self.assertEqual(championship_response.data["name"], "garcia")
        self.assertEqual(
            championship_response.data["description"], "awsgfasdverfw dffwg ffegfegdh"
        )

    def test_get_championships(self):
        response = self.client.get("/api/championships/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 1)

    def test_get_championship(self):
        championship_response = self.client.post(
            "/api/championships/", self.championship_data
        )
        championship_id = championship_response.data["id"]
        championship = self.client.get(f"/api/championships/{championship_id}/")
        self.assertEqual(championship.status_code, 200)
        self.assertEqual(championship.data["award"], 9.2)
        self.assertEqual(championship.data["name"], "garcia")
        self.assertEqual(
            championship.data["description"], "awsgfasdverfw dffwg ffegfegdh"
        )

    def test_update_championships(self):
        championship_response = self.client.post(
            "/api/championships/", self.championship_data
        )
        championship_id = championship_response.data["id"]
        championship_update = self.client.patch(
            f"/api/championships/{championship_id}/", {"name": "PATH championship"}
        )
        self.assertEqual(championship_update.status_code, 200)
        self.assertEqual(championship_update.data["name"], "PATH championship")

    def test_delete_championship(self):
        championship_response = self.client.post(
            "/api/championships/", self.championship_data
        )

        championship_id = championship_response.data["id"]
        championship_delete = self.client.delete(
            f"/api/championships/{championship_id}/"
        )
        self.assertEqual(championship_delete.status_code, 204)
