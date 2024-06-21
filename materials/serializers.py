from rest_framework import serializers

from materials.models import Section, Material


class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = "__all__"


class SectionSerializer(serializers.ModelSerializer):
    materials_count = serializers.SerializerMethodField()
    materials = serializers.SerializerMethodField()

    def get_materials_count(self, section):
        return Material.objects.filter(section=section).count()

    def get_materials(self, section):
        return [material.title for material in Material.objects.filter(section=section)]

    class Meta:
        model = Section
        fields = ['id', 'title', 'picture', 'description', 'materials_count', "materials",]
