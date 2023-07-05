from django.contrib import admin

from apps.commons.admin import SingleImageInline
from apps.contacts.models import Contacts, Connection, SocialLinks


class ImageInline(SingleImageInline):
    verbose_name = 'пункт'
    verbose_name_plural = 'Лого соцсети'


@admin.register(SocialLinks)
class SocialLinksAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)


class ConnectionInline(admin.StackedInline):
    model = Connection
    extra = 0

    verbose_name = 'элемент'
    verbose_name_plural = 'Дополнительные данные для связи'


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    inlines = (ConnectionInline,)

