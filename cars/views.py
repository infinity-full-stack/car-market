from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import CarBrand, Car
from .serializers import CarBrandSerializer, CarSerializer


class CarBrandListCreateView(ListCreateAPIView):
    serializer_class = CarBrandSerializer

    def get_queryset(self):
        return CarBrand.objects.all()


class CarBrandDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarBrandSerializer

    def get_queryset(self):
        return CarBrand.objects.all()


class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        queryset = Car.objects.all()

        brand_id = self.request.query_params.get('brand_id')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if brand_id:
            queryset = queryset.filter(brand_id=brand_id)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset


class CarDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return Car.objects.all()
