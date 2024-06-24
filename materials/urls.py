from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from materials.apps import MaterialsConfig
from materials.views import (MaterialListAPIView, MaterialRetrieveAPIView,
                             SectionListAPIView, SectionRetrieveAPIView)

app_name = MaterialsConfig.name

urlpatterns = [
    path("sections/", SectionListAPIView.as_view(), name="section_list"),
    path(
        "sections/<int:pk>/",
        SectionRetrieveAPIView.as_view(),
        name="section_detail",
    ),
    path("materials/", MaterialListAPIView.as_view(), name="material_list"),
    path(
        "materials/<int:pk>/",
        MaterialRetrieveAPIView.as_view(),
        name="material_detail",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
