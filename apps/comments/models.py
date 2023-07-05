from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from apps.commons.models import ImageModel
from apps.users.models import Teacher


class Comments(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    fio = models.CharField(verbose_name='ФИО ученика\студента', max_length=200)
    social_status = models.CharField(verbose_name='Специальность\Социальный статус', max_length=200)
    city = models.CharField(verbose_name='Город', max_length=200)
    comment = models.TextField(verbose_name='Текст', max_length=500)
    teacher = models.ForeignKey(Teacher, verbose_name='Отзыв на учителя', on_delete=models.SET_NULL, blank=True, null=True,)

    image = GenericRelation(
        ImageModel,
        related_name='image_student',
        verbose_name='Изображение',
        null=True
    )

    def __str__(self):
        if self.teacher:
            return f'Отзыв на преподавателя {self.teacher} от {self.fio}'
        return f'Отзыв от {self.fio}'
