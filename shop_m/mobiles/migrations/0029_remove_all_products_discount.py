# Generated by Django 4.0.3 on 2022-08-16 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0028_alter_all_products_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='all_products',
            name='discount',
        ),
    ]
