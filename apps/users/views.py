from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from apps.users.filters import TeacherFilter
from apps.users.models import Teacher
from apps.users.serializer import TeacherListSerializer, TeacherRetrieveSerializer


class PageTotalPagination(PageNumberPagination):
    page_size = 6

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })


class TeachersAPIView(ReadOnlyModelViewSet):
    queryset = Teacher.objects.filter(is_active=True)
    pagination_class = PageTotalPagination
    filter_backends = [TeacherFilter]

    action_serializers = {
        'list': TeacherListSerializer,
        'retrieve': TeacherRetrieveSerializer,
    }

    def get_serializer_class(self):
        return self.action_serializers.get(
            self.action,
            self.serializer_class
        )
