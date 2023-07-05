from apps.comments.models import Comments
from apps.commons.serializer import ImageMixinSerializer


class CommentsSerializer(ImageMixinSerializer):

    class Meta:
        model = Comments
        fields = (
            'fio',
            'social_status',
            'city',
            'comment',
            'image',
        )
