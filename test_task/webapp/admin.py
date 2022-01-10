from django.contrib import admin
from webapp.models import Card, Product, PurchasedProduct

# Register your models here.

class CardAdmin(admin.ModelAdmin):
    list_display = ['id', 'card_owner', 'card_number', 'created_at', 'end_date', 'card_status']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'price', 'created_at']

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'card', 'purchased_date']


admin.site.register(Card, CardAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(PurchasedProduct, PurchaseAdmin)