from django.urls import path
from rest_framework.routers import DefaultRouter

from tickets.apps.cars.api.views import CarViewSet


router = DefaultRouter()
router.register(r'cars', CarViewSet)

urlpatterns = [] + router.urls
