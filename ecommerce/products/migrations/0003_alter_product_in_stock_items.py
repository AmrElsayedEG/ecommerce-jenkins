# Generated by Django 3.2 on 2023-03-07 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_big_unit_items_product_in_big_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='in_stock_items',
            field=models.PositiveIntegerField(default=0),
        ),
    ]