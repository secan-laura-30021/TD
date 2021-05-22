from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_lister, name='cart_lister'),
    path('perform-command/', views.PerformCommand.as_view(), name='perform_command'),
]
