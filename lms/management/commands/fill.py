# import json
#
# from django.core.management import BaseCommand, call_command
#
#
# class Command(BaseCommand):
#     help = 'Load fixture data from payments.json into database'
#
#     def handle(self, *args, **options):
#         with open('payments.json', 'r') as file:
#             fixture_data = json.load(file)
#
#         for data in fixture_data:
#             model = data['model']
#             pk = data['pk']
#             fields = data['fields']
#
#             call_command('loaddata', '--format=json', '--ignorenonexistent',
#                          '--verbosity=0', model, pk, **fields)