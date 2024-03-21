from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from urllib.parse import urlparse


def validate_youtube_url(value):
    url_validator = URLValidator()
    try:
        url_validator(value)
        parsed_url = urlparse(value)
        if parsed_url.netloc != 'www.youtube.com':
            raise ValidationError("Ссылка должна быть на YouTube видео.")
    except ValidationError:
        raise ValidationError("Некорректная ссылка.")
