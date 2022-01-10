from django.db import models
import random
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField

from django.db.models.fields.related import ForeignKey

# Create your models here.


def random_numbers():
    rnd_num = f'1234{random.randint(5678, 5999)}{random.randint(11, 99)}'
    return rnd_num

class Card(models.Model):

    card_owner = models.CharField(
        max_length=500,
        blank=False,
        null=False,
        verbose_name='Имя Владельца Карты'
    )

    card_number = models.IntegerField(default=random_numbers,)

    card_balance = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        default=100
    )

    card_status = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата Выпуска Карты'
        )
    end_date = models.DateField(
        verbose_name='Дата Истечения Срока Карты'
    )

    class Meta:
        db_table = 'cards'
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'


class Product(models.Model):
    product_name = models.CharField(
        max_length=500,
        blank=False,
        null=False,
        verbose_name='Наименование Товара'
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=False,
        null=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата Появления Товара'
        )

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class PurchasedProduct(models.Model):
    product = models.ForeignKey(
        'webapp.Product',
        on_delete=models.CASCADE,
        related_name='product',
        verbose_name='Product'    
    )
    
    card = models.ForeignKey(
        'webapp.Card',
        on_delete=CASCADE,
        related_name='card',
        verbose_name='Card'
    )

    purchased_date = DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'purchased'
        verbose_name = 'Purchased'
        verbose_name_plural = 'Purchased'