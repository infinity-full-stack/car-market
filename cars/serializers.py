from rest_framework import serializers
from .models import CarBrand, Car, Comment


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


class CommentSerializer(serializers.ModelSerializer):
    car = CarSerializer(read_only=True)
    car_id = serializers.PrimaryKeyRelatedField(
        queryset=Car.objects.all(), source='car', write_only=True
    )

    class Meta:
        model = Comment
        fields = ['id', 'car', 'car_id', 'author', 'text', 'created_at']

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.car = validated_data.get('car', instance.car)
        instance.author = validated_data.get('author', instance.author)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance
