# Generated by Django 4.0.3 on 2022-08-14 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0025_alter_all_products_show_apple'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_products',
            name='show_huawei',
            field=models.BooleanField(default=False, verbose_name='Huawei'),
        ),
        migrations.AddField(
            model_name='all_products',
            name='show_samsung',
            field=models.BooleanField(default=False, verbose_name='Samsung'),
        ),
        migrations.AddField(
            model_name='all_products',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
