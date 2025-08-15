from django.urls import path
from amicable_pairs import views

urlpatterns = [
    path('', views.amicable_numbers_view, name='index'),
]