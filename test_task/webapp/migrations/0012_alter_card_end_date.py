# Generated by Django 4.0.1 on 2022-01-10 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_remove_card_delete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='end_date',
            field=models.DateField(verbose_name='Дата Истечения Срока Карты'),
        ),
    ]
