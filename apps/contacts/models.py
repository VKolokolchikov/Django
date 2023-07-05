from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from apps.commons.models import ImageModel


class Contacts(models.Model):
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    address = models.CharField(verbose_name='Адрес', max_length=200)
    work_time = models.CharField(verbose_name='Время работы', max_length=300)

    @classmethod
    def get_default_pk(cls):
        contact = cls.objects.first()
        if contact:
            return contact.pk


class Connection(models.Model):
    PHONE = 1
    EMAIL = 2

    CHOICES = (
        (PHONE, 'Телефон'),
        (EMAIL, 'Email'),
    )

    contact = models.ForeignKey(
        Contacts,
        on_delete=models.CASCADE,
        related_name='connections',
        default=Contacts.get_default_pk
    )
    type_connection = models.IntegerField(verbose_name='Тип связи', choices=CHOICES)
    text = models.CharField(verbose_name='Данные для связи', max_length=150)


class SocialLinks(models.Model):
    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'

    contact = models.ForeignKey(
        Contacts,
        on_delete=models.CASCADE,
        related_name='social_links',
        default=Contacts.get_default_pk
    )
    image = GenericRelation(
        ImageModel,
        related_name='image_social_links',
        verbose_name='Изображение',
        null=True
    )
    link = models.CharField(verbose_name='Ссылка', max_length=1024)
