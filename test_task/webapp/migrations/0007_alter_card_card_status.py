# Generated by Django 4.0.1 on 2022-01-09 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_alter_card_card_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_status',
            field=models.BooleanField(default=False),
        ),
    ]
