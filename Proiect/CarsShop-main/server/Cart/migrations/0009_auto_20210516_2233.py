# Generated by Django 3.1.7 on 2021-05-16 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_remove_product_stock'),
        ('Cart', '0008_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='Product.Product'),
        ),
    ]
