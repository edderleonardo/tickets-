from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import InfringementView


router = DefaultRouter()
router.register(r'infringements', InfringementView, basename='infringement')


urlpatterns = [] + router.urls
