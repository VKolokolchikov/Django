from  rest_framework.generics import ListAPIView

from apps.documents.models import Documents
from apps.documents.serializers import DocumentsSerializer


class DocumentsListAPIView(ListAPIView):
    serializer_class = DocumentsSerializer
    queryset = Documents.objects.all()
