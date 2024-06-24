from rest_framework import serializers

from checks.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    material_title = serializers.SerializerMethodField()

    def get_material_title(self, question):
        return question.material.title

    class Meta:
        model = Question
        fields = [
            "id",
            "question",
            "answer_right",
            "answer_wrong_1",
            "answer_wrong_2",
            "answer_wrong_3",
            "material",
            "material_title",
        ]
