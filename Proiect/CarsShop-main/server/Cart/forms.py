from django import forms
from django.contrib.auth.models import User
from Product.models import Product
from .models import Cart, Order


class CartForm(forms.ModelForm):
    product = forms.ModelChoiceField(label='', queryset=Product.objects.all())
    quantity = forms.IntegerField(label='', widget=forms.TextInput(attrs={'placeholder': 'Cantitate'}))


    class Meta:
        model = Cart

        fields = (
            'product',
            'quantity',
        )


class OrderCreateForm(forms.ModelForm):

    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Prenume'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Nume'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    address = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Adresa'}))
    postal_code = forms.IntegerField(label='', widget=forms.TextInput(attrs={'placeholder': 'Cod postal'}))
    city = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Oras'}))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
