from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema_view
from rest_framework.permissions import IsAuthenticated

from tickets.apps.civils.models import Civil
from tickets.apps.civils.api.serializers import CivilSerializer


@extend_schema(tags=['Personas'])
@extend_schema_view(
    retrieve=extend_schema(summary='Detalle de persona', description='Detalle de una persona'),
    create=extend_schema(
        summary='Crear persona', description='Crear una persona enviado el nombre y el correo electrónico'
    ),
    update=extend_schema(summary='Actualizar persona', description='Actualizar una persona'),
    partial_update=extend_schema(
        summary='Actualizar parcialmente persona', description='Actualizar parcialmente una persona'
    ),
    destroy=extend_schema(summary='Eliminar persona', description='Eliminar una persona'),
    list=extend_schema(summary='Listar personas', description='Listar todas las personas'),
)
class CivilViewSet(viewsets.ModelViewSet):
    queryset = Civil.objects.all()
    serializer_class = CivilSerializer
    permission_classes = [IsAuthenticated]
