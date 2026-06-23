from django.urls import path
from .views import (
    CarBrandListCreateView, CarBrandDetailView,
    CarListCreateView, CarDetailView,
    CommentListCreateView, CommentDetailView,
)

urlpatterns = [
    path('brands/', CarBrandListCreateView.as_view()),
    path('brands/<int:pk>/', CarBrandDetailView.as_view()),
    path('cars/', CarListCreateView.as_view()),
    path('cars/<int:pk>/', CarDetailView.as_view()),
    path('comments/', CommentListCreateView.as_view()),
    path('comments/<int:pk>/', CommentDetailView.as_view()),
]
