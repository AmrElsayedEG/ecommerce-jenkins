# Generated by Django 3.2 on 2023-03-08 20:59

from django.db import migrations, models
import django.db.models.deletion
import products.models.sub_category


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_in_stock_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='has_sub_category',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to=products.models.sub_category.sub_image)),
                ('order', models.IntegerField(default=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='products.category')),
            ],
            options={
                'verbose_name': 'sub category',
                'verbose_name_plural': 'sub categories',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.subcategory'),
        ),
    ]