from rest_framework import serializers
from .models import CarBrand, Car


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    brand = CarBrandSerializer(read_only=True)
    brand_id = serializers.PrimaryKeyRelatedField(
        queryset=CarBrand.objects.all(), source='brand', write_only=True
    )

    class Meta:
        model = Car
        fields = ['id', 'model_name', 'price', 'color', 'year', 'brand', 'brand_id']
