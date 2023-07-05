from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from apps.commons.models import DateTimeMixin, FileModel


class Documents(DateTimeMixin):
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    title = models.CharField(verbose_name='Название', max_length=200)
    file = GenericRelation(
        FileModel,
        related_name='file_documents',
        verbose_name='Изображение',
        null=True
    )
