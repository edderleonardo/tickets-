from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema_view
from rest_framework.permissions import IsAuthenticated

from tickets.apps.cars.models import Car
from tickets.apps.civils.models import Civil
from tickets.apps.cars.api.serializers import CarSerializer, CarDetailSerializer, OwnerCarsSerializer


@extend_schema(tags=['Vehículos'], description='Listado de vehículos')
@extend_schema_view(
    retrieve=extend_schema(summary='Detalle de vehículo', description='Detalle de un vehículo'),
    create=extend_schema(summary='Crear vehículo', description='Crear un vehículo'),
    update=extend_schema(summary='Actualizar vehículo', description='Actualizar un vehículo'),
    partial_update=extend_schema(
        summary='Actualizar parcialmente vehículo', description='Actualizar parcialmente un vehículo'
    ),
    destroy=extend_schema(summary='Eliminar vehículo', description='Eliminar un vehículo'),
    list=extend_schema(summary='Listar vehículos', description='Listar todos los vehículos'),\
    by_owner=extend_schema(summary='Listar vehículos por dueño', description='Devuelve una lista de vehículos pertenecientes a un propietario específico.')
)
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner']

    @action(detail=False, methods=['get'], url_path='by-owner/(?P<owner_id>\d+)')
    def by_owner(self, request, owner_id=None):
        try:
            owner = Civil.objects.get(pk=owner_id)
        except Civil.DoesNotExist:
            return Response({"detail": "Persona no encontrada."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = OwnerCarsSerializer(owner)
        return Response(serializer.data)