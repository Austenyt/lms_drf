import re

from django.core.exceptions import ValidationError


class LessonCustomValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        youtube_host_regex = re.compile(r'(www\.)?youtube\.com|youtu\.be')
        field_value = dict(value).get(self.field, '')

        if not youtube_host_regex.search(field_value):
            raise ValidationError('The link should be from YouTube hosting.')
