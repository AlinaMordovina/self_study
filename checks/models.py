from django.db import models

from config import settings
from materials.models import Material


class Question(models.Model):
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        verbose_name="Материал",
    )

    question = models.CharField(
        max_length=255,
        verbose_name="Вопрос",
    )

    answer_right = models.CharField(
        max_length=255,
        verbose_name="Правильный ответ",
    )

    answer_wrong_1 = models.CharField(
        max_length=255,
        verbose_name="Неправильный ответ 1",
    )

    answer_wrong_2 = models.CharField(
        max_length=255,
        verbose_name="Неправильный ответ 2",
    )

    answer_wrong_3 = models.CharField(
        max_length=255,
        verbose_name="Неправильный ответ 3",
    )

    def __str__(self):
        return f"{self.question}"

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Log(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="answers",
        verbose_name="Вопрос",
    )

    answer = models.CharField(
        max_length=255,
        verbose_name="Ответ",
    )

    is_right = models.BooleanField(default=False, verbose_name="Правильный ответ")

    def __str__(self):
        return f"{self.answer}"

    class Meta:
        verbose_name = "Лог ответов"
        verbose_name_plural = "Логи ответов"
