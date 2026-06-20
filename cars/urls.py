from django.urls import path
from .views import CarBrandListCreateView, CarBrandDetailView, CarListCreateView, CarDetailView

urlpatterns = [
    path('brands/', CarBrandListCreateView.as_view()),
    path('brands/<int:pk>/', CarBrandDetailView.as_view()),
    path('cars/', CarListCreateView.as_view()),
    path('cars/<int:pk>/', CarDetailView.as_view()),
]
