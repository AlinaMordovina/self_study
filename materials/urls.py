from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from materials.views import SectionViewSet, MaterialCreateAPIView, MaterialListAPIView, MaterialRetrieveAPIView, \
    MaterialUpdateAPIView, MaterialDestroyAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'sections', SectionViewSet, basename='sections')

urlpatterns = [
    path('material/create/', MaterialCreateAPIView.as_view(), name="material_create"),
    path('material/', MaterialListAPIView.as_view(), name="material_list"),
    path("material/<int:pk>/", MaterialRetrieveAPIView.as_view(), name="material_detail"),
    path("material/<int:pk>/update/", MaterialUpdateAPIView.as_view(), name="material_update"),
    path("material/<int:pk>/delete/", MaterialDestroyAPIView.as_view(), name="material_delete"),
] + router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
