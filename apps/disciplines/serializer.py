from rest_framework import serializers

from apps.disciplines.models import Disciplines


class DisciplinesListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Disciplines
        fields = (
            'id',
            'title',
            'image',
        )

    @staticmethod
    def get_image(obj, *args, **kwargs):
        return obj.image.get_current_file_url()


class DisciplinesRetrieveSerializer(DisciplinesListSerializer):
    logo = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Disciplines
        fields = (
            'id',
            'title',
            'content',
            'image',
            'logo',
            'quote',
            'author',
        )

    @staticmethod
    def get_logo(obj, *args, **kwargs):
        return obj.logo.get_current_file_url()
