# serializers.py

from rest_framework import serializers
from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `resturant` instance
        """
        return Restaurant.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Create and return a new `resturant` instance
        """
        return Restaurant.objects.create(**validated_data)
