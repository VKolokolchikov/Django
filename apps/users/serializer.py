from rest_framework import serializers

from apps.commons.serializer import ImageMixinSerializer
from apps.disciplines.serializer import DisciplinesListSerializer
from apps.users.models import Teacher, AboutTeacher, DepartmentGroup


class TeacherInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutTeacher
        fields = '__all__'


class TeacherListSerializer(ImageMixinSerializer):

    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'experience', 'image')


class TeacherRetrieveSerializer(ImageMixinSerializer):
    about_teacher = TeacherInfoSerializer(many=True, read_only=True)
    disciplines = DisciplinesListSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = (
            'id',
            'first_name',
            'last_name',
            'patronymic',
            'education',
            'experience',
            'image',
            'about_teacher',
            'disciplines'
        )

    @staticmethod
    def get_disciplines(obj):
        disciplines = DepartmentGroup.objects.select_related('disciplines').filter(teacher_id=obj.id)
        return disciplines
