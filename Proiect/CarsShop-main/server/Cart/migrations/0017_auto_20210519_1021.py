# Generated by Django 3.1.7 on 2021-05-19 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0016_auto_20210519_1020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='cantitate',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='pret',
            new_name='quantity',
        ),
    ]