# Generated by Django 2.1 on 2023-02-11 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0033_auto_20230211_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
