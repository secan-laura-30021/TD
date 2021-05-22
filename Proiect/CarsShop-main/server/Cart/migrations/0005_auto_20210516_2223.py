# Generated by Django 3.1.7 on 2021-05-16 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='Cart.Cart'),
        ),
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=True),
        ),
    ]
