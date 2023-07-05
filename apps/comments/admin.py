from django.contrib import admin

from apps.comments.models import Comments
from apps.commons.admin import SingleImageInline


class ImageInline(SingleImageInline):
    verbose_name_plural = 'Фотография ученика'


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
