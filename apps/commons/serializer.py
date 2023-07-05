from rest_framework import serializers


class ImageMixinSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_image(obj, *args, **kwargs):
        return obj.image.get_current_file_url()


class FileMixinSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_file(obj, *args, **kwargs):
        return obj.file.get_current_file_url()
