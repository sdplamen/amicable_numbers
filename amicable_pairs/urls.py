from django.urls import path
from amicable_pairs import views
from amicable_pairs.api import AmicableNumbersAPI

urlpatterns = [
    path('', views.amicable_numbers_view, name='index'),
    path('', views.amicable_numbers_view, name='index'),
    path('api/amicable-numbers/', AmicableNumbersAPI.as_view(), name='amicable_numbers_api'),
]