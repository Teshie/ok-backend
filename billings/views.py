from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated, AllowAny

class CategoryCreateList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class CategoryUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    lookup_field = 'pk'

        
class ProductCreateList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def filter_queryset(self, queryset):
        queryset = queryset.filter(user=self.request.user)
        return super().filter_queryset(queryset)

    #perform create with current user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartCreateList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def filter_queryset(self, queryset):
        queryset = queryset.filter(user=self.request.user)
        return super().filter_queryset(queryset)

    #perform create with current user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    

class StoreCreateList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def filter_queryset(self, queryset):
        queryset = queryset.filter(user=self.request.user)
        return super().filter_queryset(queryset)

    #perform create with current user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    