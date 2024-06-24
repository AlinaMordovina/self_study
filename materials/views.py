from rest_framework import viewsets, generics
import django_filters.rest_framework

from materials.models import Section, Material
from materials.pagination import MaterialsPagination
from materials.serializers import SectionSerializer, MaterialSerializer


class SectionViewSet(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all().order_by('pk')
    pagination_class = MaterialsPagination


class MaterialCreateAPIView(generics.CreateAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()


class MaterialListAPIView(generics.ListAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all().order_by('pk')
    pagination_class = MaterialsPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['section',]


class MaterialRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()


class MaterialUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()


class MaterialDestroyAPIView(generics.DestroyAPIView):
    queryset = Material.objects.all()
