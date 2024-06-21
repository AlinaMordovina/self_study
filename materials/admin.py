from django.contrib import admin

from materials.models import Section, Material


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("id", "title",)
    search_fields = (
        "title",
        "description",
    )


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("id", "title",)
    list_filter = ("section",)
    search_fields = (
        "title",
        "description",
    )
