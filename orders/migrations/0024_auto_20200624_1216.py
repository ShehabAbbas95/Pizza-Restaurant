# Generated by Django 2.1.5 on 2020-06-24 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_auto_20200622_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carts',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
