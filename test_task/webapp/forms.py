from django import forms
from django.forms import widgets
from webapp.models import Card, Product


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('card_owner', 'card_number', 'card_status', 'card_balance', 'end_date')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'price')


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Search')