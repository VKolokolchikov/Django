from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from apps.commons.models import DateTimeMixin, ImageModel, LogoModel


class Disciplines(DateTimeMixin):
    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'

    title = models.CharField(verbose_name='Название', max_length=150)
    quote = models.CharField(verbose_name='Цитата или краткое описание для заголовка', max_length=255, null=True)
    author = models.CharField(verbose_name='Автор цитаты', max_length=50, null=True)
    content = models.TextField(verbose_name='Содержимое страницы')

    image = GenericRelation(
        ImageModel,
        related_name='image_disciplines',
        verbose_name='Изображение',
        null=True
    )
    logo = GenericRelation(
        LogoModel,
        related_name='logo_disciplines',
        verbose_name='Логотип дисциплины',
        null=True
    )

    def __str__(self):
        return f'{self.id} - {self.title}'
