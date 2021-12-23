# Generated by Django 2.1.5 on 2020-06-19 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20200619_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('small', models.CharField(max_length=64)),
                ('large', models.CharField(max_length=64)),
                ('type', models.CharField(default=None, max_length=64)),
            ],
        ),
        migrations.DeleteModel(
            name='regular',
        ),
        migrations.DeleteModel(
            name='sicilian',
        ),
    ]