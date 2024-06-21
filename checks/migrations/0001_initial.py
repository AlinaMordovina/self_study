# Generated by Django 5.0.6 on 2024-06-21 20:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("materials", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.CharField(max_length=255, verbose_name="Вопрос")),
                (
                    "answer_right",
                    models.CharField(max_length=50, verbose_name="Правильный ответ"),
                ),
                (
                    "answer_wrong_1",
                    models.CharField(
                        max_length=50, verbose_name="Неправильный ответ 1"
                    ),
                ),
                (
                    "answer_wrong_2",
                    models.CharField(
                        max_length=50, verbose_name="Неправильный ответ 2"
                    ),
                ),
                (
                    "answer_wrong_3",
                    models.CharField(
                        max_length=50, verbose_name="Неправильный ответ 3"
                    ),
                ),
                (
                    "material",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.material",
                        verbose_name="Материал",
                    ),
                ),
            ],
            options={
                "verbose_name": "Вопрос",
                "verbose_name_plural": "Вопросы",
            },
        ),
        migrations.CreateModel(
            name="Answer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("answer", models.CharField(max_length=50, verbose_name="Ответ")),
                (
                    "is_right",
                    models.BooleanField(default=False, verbose_name="Правильный ответ"),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="answers",
                        to="checks.question",
                        verbose_name="Вопрос",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ответ",
                "verbose_name_plural": "Ответы",
            },
        ),
    ]