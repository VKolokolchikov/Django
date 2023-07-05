from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from apps.commons.models import BaseUserInfoMixin, ImageModel
from apps.disciplines.models import Disciplines
from apps.users.constance import TypeTeacherInfo


class Teacher(BaseUserInfoMixin, models.Model):
    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    experience = models.PositiveIntegerField(verbose_name='Стаж')
    education = models.CharField(verbose_name='Образование', max_length=200)
    disciplines = models.ManyToManyField(
        Disciplines,
        through='DepartmentGroup',
        through_fields=('teacher', 'disciplines')
    )
    image = GenericRelation(
        ImageModel,
        related_name='image_teachers',
        verbose_name='Изображение',
        null=True
    )


class AboutTeacher(models.Model):
    class Meta:
        unique_together = ('teacher', 'type_info')

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='about_teacher')
    type_info = models.CharField(verbose_name='Тип информации', choices=TypeTeacherInfo.CHOICES_TYPES, max_length=100)
    title = models.CharField(max_length=100, null=True)
    info = models.TextField(verbose_name='Основные сведения', max_length=1000)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.title = TypeTeacherInfo.TITLES[self.type_info]
        return super(AboutTeacher, self).save(force_insert, force_update, using, update_fields)


class DepartmentGroup(models.Model):
    teacher = models.ForeignKey(Teacher, verbose_name='Учитель', on_delete=models.CASCADE)
    disciplines = models.ForeignKey(Disciplines, verbose_name='Дисциплина', on_delete=models.CASCADE)
