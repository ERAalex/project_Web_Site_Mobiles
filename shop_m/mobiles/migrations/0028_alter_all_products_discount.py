# Generated by Django 4.0.3 on 2022-08-16 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0027_all_products_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_products',
            name='discount',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Размер скидки'),
        ),
    ]
