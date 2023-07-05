from django.contrib import admin

from apps.commons.admin import SingleImageInline
from apps.users.models import Teacher, AboutTeacher, DepartmentGroup


class ImageInline(SingleImageInline):
    verbose_name = 'элемент'
    verbose_name_plural = 'Фотография преподавателя'


class AboutInfoInline(admin.StackedInline):
    model = AboutTeacher
    exclude = ('title',)
    extra = 0

    verbose_name = 'элемент'
    verbose_name_plural = 'Информация о преподавателе'


class DepartmentInline(admin.TabularInline):
    model = DepartmentGroup
    extra = 0

    verbose_name = 'Предмет'
    verbose_name_plural = 'Дисциплины преподавателя'


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [AboutInfoInline, DepartmentInline, ImageInline]
