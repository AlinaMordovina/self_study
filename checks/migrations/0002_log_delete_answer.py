# Generated by Django 5.0.6 on 2024-06-24 12:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("checks", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Log",
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
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Дата"),
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
                "verbose_name": "Лог ответов",
                "verbose_name_plural": "Логи ответов",
            },
        ),
        migrations.DeleteModel(
            name="Answer",
        ),
    ]