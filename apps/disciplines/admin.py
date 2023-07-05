from ckeditor_uploader.widgets import CKEditorUploadingWidget

from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.commons.admin import SingleImageInline, SingleLogoInline
from apps.disciplines.models import Disciplines


class ImageInline(SingleImageInline):
    verbose_name = "Изображение"
    verbose_name_plural = "Логотип для панели"


class LogoInline(SingleLogoInline):
    verbose_name = "Изображение"
    verbose_name_plural = "Логотип в заголовке"


class DisciplinesForm(forms.ModelForm):
    content = forms.CharField(label='Содержимое страницы', widget=CKEditorUploadingWidget())

    class Meta:
        model = Disciplines
        fields = '__all__'


@admin.register(Disciplines)
class DisAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'id', 'title',)
    list_display_links = ('get_image', 'id', 'title')
    readonly_fields = ('get_image',)

    fieldsets = (
        ('Для заголовка', {'fields': ('quote', 'author')}),
        ('Дисциплина', {'fields': ('get_image', 'title')}),
        ('Содержание', {'fields': ('content',)}),
    )

    form = DisciplinesForm
    inlines = [ImageInline, LogoInline]

    def get_image(self, obj):
        if logo := obj.image.get_current_file_url():
            return mark_safe(f'<img src={logo} width="50" height="50">')
        return

    get_image.short_description = 'Лого'
