from django.contrib import admin

from apps.commons.admin import SingleFileInline
from apps.documents.models import Documents


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    inlines = (SingleFileInline,)
