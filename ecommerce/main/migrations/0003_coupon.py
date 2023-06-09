# Generated by Django 3.2 on 2023-03-07 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_banners_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('discount_type', models.CharField(choices=[('PER', 'Percentage'), ('Mon', 'Money')], default='PER', max_length=20)),
                ('discount', models.IntegerField(default=0)),
                ('end_date', models.DateTimeField()),
                ('total_must_be', models.FloatField(blank=True, null=True, verbose_name='Total must be equal or above')),
                ('public', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'coupon',
                'verbose_name_plural': 'coupons',
            },
        ),
    ]
