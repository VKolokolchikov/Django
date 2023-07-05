from django.db.models import Subquery
from rest_framework.filters import BaseFilterBackend

from apps.users.models import DepartmentGroup


class TeacherFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        if _id := request.query_params.get('discipline_id'):
            teachers_ids = DepartmentGroup.objects.filter(disciplines_id=_id).values('teacher_id')
            queryset = queryset.filter(id__in=Subquery(teachers_ids))
        return queryset
