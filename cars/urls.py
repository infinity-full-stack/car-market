from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CarBrandViewSet, CarViewSet, CommentViewSet

router = SimpleRouter()
router.register('brands', CarBrandViewSet)
router.register('cars', CarViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cars/brand/<int:brand_id>/', CarViewSet.as_view({'get': 'list'})),
    path('cars/<int:car_id>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
]
