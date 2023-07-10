from django.urls import path
from apps.client.api.views.register_views import create_client_api_view
from apps.client.api.views.plants_views import view_plant_api_view,list_plants_api_view


urlpatterns = [
    path('register/', create_client_api_view, name ='register'),
    path('plants/', list_plants_api_view, name ='plants'),
    path('plants/<int:pk>/', view_plant_api_view, name ='plant_retrieve')
]