from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'Create user groups in the database'

    def handle(self, *args, **options):
        # Проверяем, существует ли группа "Модераторы", и создаем ее, если нет
        moderator_group, created = Group.objects.get_or_create(name='Модераторы')
        if created:
            self.stdout.write(self.style.SUCCESS('Группа "Модераторы" успешно создана'))
        else:
            self.stdout.write(self.style.WARNING('Группа "Модераторы" уже существует'))
