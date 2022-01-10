from django.urls import path

from webapp.views import (
    CardView,
    CardOwnerDetailView,
    CardCreateView,
    CardDeleteView,
    CardDeactivateView
)

from webapp.product import(
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductDeleteView
)

app_name = 'webapp'

urlpatterns = [
    path('', CardView.as_view(), name='card_list'),
    path('card/<int:pk>/', CardOwnerDetailView.as_view(), name='card_owner'),
    path('card/create/', CardCreateView.as_view(), name='card_create'),
    path('card/<int:pk>/card_delete', CardDeleteView.as_view(), name='card_delete'),
    path('card/list/to/activate/', CardDeactivateView.as_view(), name='list_to_activate'),
    path('product/list', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/detail/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete')
]