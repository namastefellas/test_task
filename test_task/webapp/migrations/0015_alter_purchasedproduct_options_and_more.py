# Generated by Django 4.0.1 on 2022-01-10 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_purchasedproduct'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchasedproduct',
            options={'verbose_name': 'Purchased', 'verbose_name_plural': 'Purchased'},
        ),
        migrations.AlterModelTable(
            name='purchasedproduct',
            table='purchased',
        ),
    ]
