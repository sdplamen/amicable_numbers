from django.urls import path
from amicable_pairs import views
from amicable_pairs.api import AmicableNumbersAPI
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('', views.amicable_numbers_view, name='index'),
    path('api/amicable-numbers/', AmicableNumbersAPI.as_view(), name='amicable-numbers-api'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]