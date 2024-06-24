from django.contrib import admin

from checks.models import Log, Question


@admin.register(Question)
class SectionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "question",
    )
    list_filter = ("material",)
    search_fields = (
        "question",
        "answer_right",
        "answer_wrong_1",
        "answer_wrong_2",
        "answer_wrong_3",
    )


@admin.register(Log)
class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "user",
        "question",
        "answer",
        "is_right",
    )
    list_filter = ("created_at", "is_right")
    search_fields = (
        "question",
        "answer",
    )
