from django.shortcuts import render
from django.http import HttpResponse, Http404
from Product.models import Product
from Cart.models import Cart, Order
from .serializers import ProductSerializer, CartSerializer, OrderSerializer

from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter


class ProductsList(APIView):

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetails(APIView):

    def get_post(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = ProductSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        products = self.get_post(pk)
        serializer = ProductSerializer(products, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_post(pk)
        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class CartsList(APIView):

    def get(self, request, format=None):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CartSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartDetails(APIView):

    def get_post(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = CartSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        carts = self.get_post(pk)
        serializer = CartSerializer(carts, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cart = self.get_post(pk)
        cart.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class OrdersList(APIView):

    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetails(APIView):

    def get_post(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = OrderSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        orders = self.get_post(pk)
        serializer = OrderSerializer(orders, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        order = self.get_post(pk)
        order.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
