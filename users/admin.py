from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone", "avatar", "country")
    list_filter = ("country",)
    search_fields = (
        "email",
        "phone",
    )
