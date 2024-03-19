from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='номер телефона', blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name='город', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Пользователь')
    payment_date = models.DateField(verbose_name='Дата оплаты', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс', null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Отдельно оплаченный урок', null=True,
                               blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=20, choices=(('cash', 'Наличные'), ('transfer', 'Перевод на счет')),
                                      verbose_name='Способ оплаты')

    def __str__(self):
        return f"{self.user}: ({self.course if self.course else self.lesson})"

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
