# Generated by Django 2.0.2 on 2018-07-31 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_personalnote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='url',
        ),
    ]