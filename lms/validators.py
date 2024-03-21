from django.core.exceptions import ValidationError


class LessonLinkValidator:
    def __init__(self, allowed_domain):
        self.allowed_domain = allowed_domain

    def __call__(self, value):
        if not value.startswith(f'https://www.{self.allowed_domain}/'):
            raise ValidationError(f'Only links to {self.allowed_domain} are allowed.')
