from apps.documents.models import Documents
from apps.commons.serializer import FileMixinSerializer


class DocumentsSerializer(FileMixinSerializer):

    class Meta:
        model = Documents
        fields = ('title', 'file')
