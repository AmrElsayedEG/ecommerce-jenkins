# Generated by Django 3.2 on 2023-03-12 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='default',
            field=models.BooleanField(default=True),
        ),
    ]
