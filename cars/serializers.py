from rest_framework import serializers
from .models import Brand, Car


class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
