import django_filters.rest_framework
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from checks.models import Log, Question
from checks.serializers import QuestionSerializer
from checks.pagination import ChecksPagination


class QuestionListAPIView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all().order_by('pk')
    pagination_class = ChecksPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = [
        "material",
    ]


class QuestionRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class CheckAnswerAPIView(APIView):
    def post(self, *args, **kwargs):
        user = self.request.user
        question_id = self.request.data.get("question")
        question_item = get_object_or_404(Question, pk=question_id)
        answer = self.request.data.get("answer")
        answer_right = question_item.answer_right

        if answer == answer_right:
            is_right = True
            message = "Ответ верный"
        else:
            is_right = False
            message = "Ответ не верный"

        Log.objects.create(
            user=user, question=question_item, answer=answer, is_right=is_right
        )

        return Response(message)
