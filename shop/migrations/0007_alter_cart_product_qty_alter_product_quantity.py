# Generated by Django 5.1.6 on 2025-03-14 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product_qty',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
