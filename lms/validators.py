from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


class UrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        url_validator = URLValidator()
        url_validator(value)
        if self.field not in value:
            raise ValidationError("Only YouTube links are allowed.")
