from django.urls import path
from rest_framework.routers import DefaultRouter

from tickets.apps.civils.api.views import CivilViewSet


router = DefaultRouter()
router.register(r'civils', CivilViewSet)

urlpatterns = [] + router.urls
