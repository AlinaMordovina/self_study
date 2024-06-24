from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from checks.models import Log, Question
from materials.models import Material
from users.models import User


class QuestionTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email="test@test.ru", password="5462")
        self.client.force_authenticate(user=self.user)
        self.material = Material.objects.create(title="test_material")
        self.question = Question.objects.create(
            material=self.material,
            question="test_question",
            answer_right="test_answer_right",
            answer_wrong_1="test_wrong_1",
            answer_wrong_2="test_wrong_2",
            answer_wrong_3="test_wrong_3",
        )
        self.user_answer = "test_user_answer"

    def test_retrieve_question(self):
        url = reverse("checks:question_detail", args=(self.question.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data.get("question"), self.question.question)

    def test_list_question(self):
        url = reverse("checks:question_list")
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
                        "id": self.question.id,
                        "question": "test_question",
                        "answer_right": "test_answer_right",
                        "answer_wrong_1": "test_wrong_1",
                        "answer_wrong_2": "test_wrong_2",
                        "answer_wrong_3": "test_wrong_3",
                        "material": self.material.id,
                        "material_title": "test_material",
                    }
                ],
            },
        )

    def test_check_answer(self):
        data = {
            "user": self.user.id,
            "question": self.question.id,
            "answer": self.user_answer,
        }
        url = reverse("checks:check_answer", args=(self.question.pk,))
        self.client.post(url, data=data)
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            Log.objects.filter(user=self.user.id, question=self.question.id).exists(),
            True,
        )
