from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cars.urls')),
    path('auth/', include('djoser.urls')),
    path('authentication/', include('djoser.urls.authtoken')),
]
