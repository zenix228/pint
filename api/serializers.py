from rest_framework import serializers
from app.models import Category, Product, CustomUser
        

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'