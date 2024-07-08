from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated

from tickets.apps.officers.models import Officer
from tickets.apps.officers.api.serializers import OfficerSerializer


@extend_schema(tags=['Oficiales'])
class OfficerViewSet(viewsets.ModelViewSet):
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer
    permission_classes = [IsAuthenticated]
