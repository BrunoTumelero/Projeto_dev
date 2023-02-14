# Generated by Django 2.1 on 2023-02-13 23:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0037_merge_20230213_2343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='email_owner',
            new_name='email_company',
        ),
        migrations.RemoveField(
            model_name='company',
            name='name_owner',
        ),
        migrations.RemoveField(
            model_name='company',
            name='phone_owner',
        ),
        migrations.AlterField(
            model_name='company',
            name='cpf_owner',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='usersession',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session_user', to=settings.AUTH_USER_MODEL),
        ),
    ]