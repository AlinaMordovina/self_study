from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=250, verbose_name="Наименование раздела")
    picture = models.ImageField(
        upload_to="materials/sections",
        blank=True,
        null=True,
        verbose_name="Изображение",
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание раздела"
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"
        ordering = ("title",)


class Material(models.Model):
    title = models.CharField(max_length=250, verbose_name="Наименование материала")
    picture = models.ImageField(
        upload_to="materials/lessons", blank=True, null=True, verbose_name="Изображение"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание материала"
    )

    section = models.ForeignKey(
        Section, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Раздел"
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"
        ordering = ("title",)
