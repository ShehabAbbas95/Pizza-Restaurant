# Generated by Django 2.1.5 on 2020-06-27 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0035_auto_20200626_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='comment',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='carts',
            name='item_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carts',
            name='p_s_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carts',
            name='subs_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='item_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='p_s_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='subs_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
