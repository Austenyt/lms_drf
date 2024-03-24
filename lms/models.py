from django.db import models

from config import settings


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    preview = models.ImageField(upload_to='previews/', verbose_name='превью', blank=True, null=True)
    description = models.CharField(max_length=150, verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', null=True,
                              blank=True)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.CharField(max_length=150, verbose_name='Описание')
    preview = models.ImageField(upload_to='previews/', verbose_name='превью', blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', null=True, blank=True)
    video_url = models.URLField(verbose_name='ссылка на видео', null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', null=True,
                              blank=True)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Subscription(models.Model):
    is_subscribed = models.BooleanField(default=False, verbose_name='подписка', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь', null=True,
                             blank=True)
    course = models.ForeignKey('lms.Course', on_delete=models.CASCADE, verbose_name='курс', null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.course}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
