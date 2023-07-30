from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from apps.commons.managers import FileQuerySet
from apps.commons.utils import set_upload_path, set_extension
from apps.commons.validators import FILE_VALIDATORS, IMAGE_VALIDATORS


class DateTimeMixin(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)


class BaseUserInfoMixin(DateTimeMixin, models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(verbose_name='Имя', max_length=200)
    last_name = models.CharField(verbose_name='Фамилия', max_length=200)
    patronymic = models.CharField(verbose_name='Отчество', max_length=200)

    is_active = models.BooleanField(verbose_name='Активность пользователя', default=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'


class FileInterfaceModel(DateTimeMixin):
    class Meta:
        abstract = True

    file = models.FileField(verbose_name='Файл', validators=[], upload_to=set_upload_path)
    extension = models.CharField(max_length=25, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.IntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    objects = FileQuerySet.as_manager()

    def save(self, *args, **kwargs):
        self.extension = set_extension(self)
        if self.file and (this := self._meta.model.objects.filter(id=self.id)):
            this.first().file.delete(False)
        super(FileInterfaceModel, self).save(*args, **kwargs)

    @property
    def url(self):
        return self.file.url


class ImageModel(FileInterfaceModel):
    file = models.FileField(verbose_name='Изображение', validators=IMAGE_VALIDATORS, upload_to=set_upload_path)


class LogoModel(FileInterfaceModel):
    file = models.FileField(verbose_name='Логотип', validators=IMAGE_VALIDATORS, upload_to=set_upload_path)


class FileModel(FileInterfaceModel):
    file = models.FileField(verbose_name='Файл', validators=FILE_VALIDATORS, upload_to=set_upload_path)
