from rest_framework import serializers
from django.contrib.auth.models import User
from restaurant.models import *

class UserSeralizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name', 'last_name']

class CategorySerailizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.RelatedField(source = 'Category', read_only = True)
    category = CategorySerailizer(read_only = True)
    category_id = serializers.IntegerField(write_only = True)
    class Meta:
        model = MenuItem    
        fields = ['id', 'name', 'price','description','category', 'category_id']
