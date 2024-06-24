import django_filters.rest_framework
from rest_framework import generics

from materials.models import Material, Section
from materials.pagination import MaterialsPagination
from materials.serializers import MaterialSerializer, SectionSerializer


class SectionListAPIView(generics.ListAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all().order_by("pk")
    pagination_class = MaterialsPagination


class SectionRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()


class MaterialListAPIView(generics.ListAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all().order_by("pk")
    pagination_class = MaterialsPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = [
        "section",
    ]


class MaterialRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
