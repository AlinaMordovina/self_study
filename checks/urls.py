from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from checks.apps import ChecksConfig
from checks.views import (CheckAnswerAPIView, QuestionListAPIView,
                          QuestionRetrieveAPIView)

app_name = ChecksConfig.name

urlpatterns = [
    path("", QuestionListAPIView.as_view(), name="question_list"),
    path("<int:pk>/", QuestionRetrieveAPIView.as_view(), name="question_detail"),
    path("<int:pk>/check_answer/", CheckAnswerAPIView.as_view(), name="check_answer"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
