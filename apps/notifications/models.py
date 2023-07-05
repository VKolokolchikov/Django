from django.db import models

from apps.commons.models import DateTimeMixin
from apps.commons.validators import phone_validator
from apps.notifications.constance import StatusComment


class Notifications(DateTimeMixin):

    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Завка на звонок'

    fio = models.CharField(verbose_name='ФИО', max_length=200)
    phone = models.CharField(verbose_name='Номер телефона', validators=[phone_validator], max_length=100)

    comment = models.TextField(verbose_name='Комментарий менеджера', max_length=500, null=True, blank=True)
    status_comment = models.IntegerField(
        verbose_name='Статус заявки',
        choices=StatusComment.CHOICES,
        default=StatusComment.UNPROCESSED
    )

    def __str__(self):
        return f'Заявка от {self.fio}. Статус: {StatusComment.TITLES[self.status_comment]}'
