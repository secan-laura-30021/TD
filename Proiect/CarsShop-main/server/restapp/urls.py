from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('products/', views.ProductsList.as_view(), name='products_list'),
    path('products/<int:pk>', views.ProductDetails.as_view(), name='product_details'),
    path('carts/', views.CartsList.as_view(), name='carts_list'),
    path('carts/<int:pk>', views.CartDetails.as_view(), name='cart_details'),
    path('orders/', views.OrdersList.as_view(), name='orders_list'),
    path('orders/<int:pk>', views.OrderDetails.as_view(), name='order_details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
