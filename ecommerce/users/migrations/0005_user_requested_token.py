# Generated by Django 3.2 on 2023-03-06 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='requested_token',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
