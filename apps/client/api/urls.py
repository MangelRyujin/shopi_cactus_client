from django.urls import path
from apps.client.api.views.client_views import list_client_api_view, create_client_api_view



urlpatterns = [
    path('clients/', list_client_api_view, name = 'clients' ),
    path('register/', create_client_api_view, name ='register'),

]