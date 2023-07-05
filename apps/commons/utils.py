import re

from apps.commons.constances import ValidExtension


def set_upload_path(instance, filename):
    path = instance.content_object.__class__.__name__.lower()
    return f'{path}/{instance.content_object.id}/{filename}'


def set_extension(instance):
    pattern = rf'\.({"|".join(ValidExtension.ALL)})'
    match = re.search(pattern, instance.file.name)
    extension = match.group()
    return extension[1:]
