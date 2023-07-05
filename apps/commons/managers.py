from django.db.models import QuerySet


class FileQuerySet(QuerySet):
    def get_current_file_url(self):
        if obj := self.last():
            return obj.url
