# Generated by Django 2.1.5 on 2020-06-22 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_plate'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('size', models.CharField(max_length=64)),
                ('type', models.CharField(max_length=64)),
                ('topping', models.CharField(max_length=64)),
                ('second_topping', models.CharField(max_length=64, null=True)),
                ('third_topping', models.CharField(max_length=64, null=True)),
                ('subs', models.CharField(max_length=64, null=True)),
                ('mark', models.CharField(max_length=64, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]