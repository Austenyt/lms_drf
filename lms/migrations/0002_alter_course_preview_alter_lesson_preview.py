# Generated by Django 5.0.3 on 2024-03-11 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='previews/', verbose_name='превью'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='previews/', verbose_name='превью'),
        ),
    ]
