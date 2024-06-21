from django.urls import path
from . import views

urlpatterns = [
    path('api/all/', views.RestaurantAllView.as_view(), name='list all'),
    path('api/create/', views.RestaurantCreateView.as_view(), name='create restaurant'),
    path('api/update/', views.RestaurantUpdateView.as_view(), name='updated restaurant'),
    path('api/delete/<id>', views.RestaurantDeleteView.as_view(), name='updated restaurant'),
    path('restaurants/statistics', views.RestaurantStatisticsView.as_view(), name='statistics'),
]