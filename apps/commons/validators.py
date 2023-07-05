import re

from django.core.validators import BaseValidator, FileExtensionValidator


MB = 2 * 1024**2

MAX_IMAGE_SIZE = 5 * MB
MAX_FILE_SIZE = 10 * MB


class BaseSizeValidator(BaseValidator):
    message = 'Максимальный размер файла - {}'

    def __init__(self, limit_value, message=None):
        super(BaseSizeValidator, self).__init__(limit_value, message)
        self.message = self.message.format(self._int_to_megabytes(limit_value))

    @staticmethod
    def _int_to_megabytes(limit_value):
        return f'{limit_value / (1024 * 2)} MB'

    def compare(self, value, valid_size):
        return value.size > valid_size


class RegexValidatorPhone(BaseValidator):
    message = 'Некорректный номер телефона'

    def compare(self, phone, valid_phone):
        return not re.match(valid_phone, phone)


# IMAGE_VALIDATORS = [FileExtensionValidator('png', 'jpg', 'jpeg'), BaseSizeValidator(MAX_IMAGE_SIZE)]
FILE_VALIDATORS = [FileExtensionValidator(['doc', 'docx', 'pdf']), BaseSizeValidator(MAX_FILE_SIZE)]
phone_validator = RegexValidatorPhone(limit_value=r'^(\+7|8)[0-9]{9}')
