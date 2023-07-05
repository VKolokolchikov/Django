from rest_framework import serializers

from apps.contacts.models import Contacts, Connection, SocialLinks
from apps.commons.serializer import ImageMixinSerializer


class SocialLinksSerializer(ImageMixinSerializer):

    class Meta:
        model = SocialLinks
        fields = ('link', 'image')


class ConnectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Connection
        fields = ('type_connection', 'text')


class ContactsSerializer(serializers.ModelSerializer):
    social_links = SocialLinksSerializer(read_only=True, many=True)
    connections = ConnectionSerializer(read_only=True, many=True)

    class Meta:
        model = Contacts
        fields = (
            'social_links',
            'connections',
            'address',
            'work_time'
        )
