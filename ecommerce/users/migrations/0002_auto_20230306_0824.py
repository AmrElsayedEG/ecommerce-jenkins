# Generated by Django 3.2 on 2023-03-06 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=1, help_text='should be alpha only with max length 50', max_length=150, verbose_name='name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=2, help_text='should be alpha only with max length 50', max_length=150, verbose_name='name'),
            preserve_default=False,
        ),
    ]