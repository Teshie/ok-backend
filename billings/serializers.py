from rest_framework import serializers
from .models import *
from accounts.serializers import AccountSerializer

class CategorySerializer(serializers.ModelSerializer):
    # name = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'user', 'name', 'imgUrl', 'selling_price', 'actual_price', 'quantity', 'get_profit']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'name', 'imgUrl', 'selling_price', 'actual_price', 'quantity', 'get_profit', 'date']

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'imgUrl', 'selling_price', 'actual_price', 'quantity',  'get_profit']







