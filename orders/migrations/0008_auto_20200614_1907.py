# Generated by Django 2.1.5 on 2020-06-14 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200614_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pasta_salads',
            old_name='name',
            new_name='n',
        ),
    ]
