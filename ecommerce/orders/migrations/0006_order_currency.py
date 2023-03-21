# Generated by Django 3.2 on 2023-03-12 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_currency_default'),
        ('orders', '0005_auto_20230310_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.currency'),
        ),
    ]
