# Generated by Django 3.2 on 2023-03-06 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='big_unit_items',
            new_name='in_big_items',
        ),
    ]