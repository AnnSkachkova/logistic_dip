# Generated by Django 5.0.4 on 2024-05-12 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delivery',
            options={'ordering': ['-expected_arrival'], 'verbose_name': 'Поставка', 'verbose_name_plural': 'Поставки'},
        ),
        migrations.AlterModelOptions(
            name='deliveryproduct',
            options={'ordering': ['delivery'], 'verbose_name': 'Продукт поставки', 'verbose_name_plural': 'Продукты поставки'},
        ),
    ]
