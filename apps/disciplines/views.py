from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.disciplines.models import Disciplines
from apps.disciplines.serializer import DisciplinesListSerializer, DisciplinesRetrieveSerializer


class DisciplinesAPIView(ReadOnlyModelViewSet):
    queryset = Disciplines.objects.all()
    action_serializers = {
        'list': DisciplinesListSerializer,
        'retrieve': DisciplinesRetrieveSerializer,
    }

    def get_queryset(self):
        queryset = super(DisciplinesAPIView, self).get_queryset()
        if self.action == 'list':
            return queryset.defer('content')
        return queryset

    def get_serializer_class(self):
        return self.action_serializers.get(
            self.action,
            self.serializer_class
        )
