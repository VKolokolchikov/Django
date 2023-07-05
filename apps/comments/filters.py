from rest_framework.filters import BaseFilterBackend


class CommentFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        if _id := request.query_params.get('teacher_id'):
            queryset = queryset.filter(teacher_id=_id)
        return queryset
