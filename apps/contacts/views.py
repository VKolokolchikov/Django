from rest_framework.views import APIView
from rest_framework.response import Response

from apps.contacts.models import Contacts
from apps.contacts.serializer import ContactsSerializer


class ContactsAPIView(APIView):
    model = Contacts
    serializer = ContactsSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = (
            self.model.objects
            .prefetch_related('connections', 'social_links')
        )
        return queryset.first()

    def get(self, request, *args, **kwargs):
        serializer = self.serializer(self.get_queryset())
        return Response(data=serializer.data)
