# Generated by Django 2.1 on 2023-01-14 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_user',
            new_name='is_consumer',
        ),
    ]
