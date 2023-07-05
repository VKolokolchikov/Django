from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny

from apps.comments.filters import CommentFilter
from apps.comments.models import Comments
from apps.comments.serializer import CommentsSerializer


class CommentsAPIView(ListAPIView):
    """Выгрузка комментариев """

    queryset = Comments.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]
    serializer_class = CommentsSerializer
    filter_backends = [CommentFilter]
