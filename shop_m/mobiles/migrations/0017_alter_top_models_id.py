# Generated by Django 4.0.3 on 2022-07-28 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0016_alter_all_products_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='top_models',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
