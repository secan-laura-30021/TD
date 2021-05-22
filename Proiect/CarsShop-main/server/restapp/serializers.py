from Product.models import *
from Cart.models import *
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'serie_sasiu', 'description', 'price', 'available',
        'an_fabricatie', 'motorizare', 'caroserie', 'kilometraj', 'putere',
        'capacitate_cilindrica', 'norma_de_poluare', 'numar_portiere', 'culoare',
        'tara_de_origine', 'data_primei_inmatriculari', 'oferit_de', 'stare',
        'created', 'updated', 'slug')


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
