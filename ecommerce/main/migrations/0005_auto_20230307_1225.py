# Generated by Django 3.2 on 2023-03-07 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_city_country'),
        ('main', '0004_shippingfee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingfee',
            name='country',
        ),
        migrations.AlterField(
            model_name='shippingfee',
            name='city',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_fees', to='users.city'),
        ),
    ]
