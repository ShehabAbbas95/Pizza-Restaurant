# Generated by Django 2.1.5 on 2020-06-19 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_remove_orders_subs'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='subs',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
