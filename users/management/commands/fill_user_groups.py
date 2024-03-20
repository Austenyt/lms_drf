from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'Заполнение базы данных групп'

    def handle(self, *args, **options):
        # Логика для заполнения созданных групп в базе данных
        groups = ['Group1', 'Group2', 'Group3']  # Список созданных групп
        for group_name in groups:
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Группа "{group_name}" создана успешно'))
            else:
                self.stdout.write(self.style.WARNING(f'Группа "{group_name}" уже существует'))
