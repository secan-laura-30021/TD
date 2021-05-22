from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.ProductsLister.as_view(), name='products_lister'),
    path('product/<slug:slug>/', views.ProductDetails.as_view(), name='product_details'),
    url(r'^signup/$', views.signup, name='signup'),
]
