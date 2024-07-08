from django.urls import path
from rest_framework import routers

from tickets.apps.officers.api.views import OfficerViewSet


router = routers.DefaultRouter()
router.register(r'officers', OfficerViewSet)

urlpatterns = [] + router.urls
