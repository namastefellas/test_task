# Generated by Django 4.0.1 on 2022-01-09 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_card_card_number_alter_goods_used_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=500, verbose_name='Наименование Товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'products',
            },
        ),
        migrations.AlterModelOptions(
            name='card',
            options={'verbose_name': 'Card', 'verbose_name_plural': 'Cards'},
        ),
        migrations.AddField(
            model_name='card',
            name='card_balance',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=5),
        ),
        migrations.AlterModelTable(
            name='card',
            table='cards',
        ),
        migrations.DeleteModel(
            name='Goods',
        ),
    ]