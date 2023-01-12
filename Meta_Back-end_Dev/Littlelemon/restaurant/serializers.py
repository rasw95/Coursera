from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['username','first_name','last_name','group']


class MenuSerializer(serializers.ModelSerializer):
    class Meta: 
        model = menu
        fields = ['Title', 'Price', 'Inventory']

class BookingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = booking
        fields = '__all__'