from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from materials.models import Material, Section
from users.models import User


class MaterialsTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email="test@test.ru", password="5462")
        self.client.force_authenticate(user=self.user)
        self.section = Section.objects.create(title="test_section")
        self.material = Material.objects.create(
            title="test_material", section=self.section
        )

    def test_retrieve_material(self):
        url = reverse("materials:material_detail", args=(self.material.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data.get("title"), self.material.title)

    def test_list_material(self):
        url = reverse("materials:material_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.material.id,
                        "title": "test_material",
                        "picture": None,
                        "description": None,
                        "section": self.section.id,
                        "section_title": self.section.title,
                    }
                ],
            },
        )


class SectionTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email="test@test.ru", password="5462")
        self.client.force_authenticate(user=self.user)
        self.section = Section.objects.create(title="test_section")
        self.material = Material.objects.create(
            title="test_material", section=self.section
        )

    def test_retrieve_section(self):
        url = reverse("materials:section_detail", args=(self.section.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data.get("title"), self.section.title)

    def test_list_section(self):
        url = reverse("materials:section_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.section.id,
                        "title": "test_section",
                        "picture": None,
                        "description": None,
                        "materials_count": 1,
                        "materials": ["test_material"],
                    }
                ],
            },
        )
