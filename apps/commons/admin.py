from django.contrib.contenttypes.admin import GenericTabularInline, InlineModelAdmin

from apps.commons.models import ImageModel, FileModel, LogoModel


class AddPermissionImageInline(InlineModelAdmin):
    target_field = 'image'

    def has_add_permission(self, request, obj=None):
        file = getattr(obj, self.target_field, None)
        if not obj or file.count() < 1:
            return super(AddPermissionImageInline, self).has_add_permission(request, obj)
        return False


class AddPermissionLogoInline(AddPermissionImageInline):
    target_field = 'logo'


class AddPermissionFileInline(AddPermissionImageInline):
    target_field = 'file'


class SingleImageInline(GenericTabularInline, AddPermissionImageInline):
    model = ImageModel
    extra = 0
    exclude = ('extension',)

    verbose_name = 'элемент'
    verbose_name_plural = 'Изображение\фото'


class SingleLogoInline(SingleImageInline, AddPermissionLogoInline):
    model = LogoModel


class SingleFileInline(GenericTabularInline, AddPermissionFileInline):
    model = FileModel
    extra = 0
    exclude = ('extension',)

    verbose_name = 'файл'
    verbose_name_plural = 'документ\файл'
