from rest_framework.routers import DefaultRouter
from apps.client.api.views.cart_viewset import CarViewSet
from apps.client.api.views.client_viewset import ClientViewSet



router = DefaultRouter()
router.register(r'client',ClientViewSet, basename = 'client')
router.register(r'my_car',CarViewSet, basename = 'my_car')





urlpatterns = router.urls 