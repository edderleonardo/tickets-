from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema_view
from rest_framework.permissions import IsAuthenticated

from tickets.apps.cars.models import Car
from tickets.apps.cars.api.serializers import CarSerializer


@extend_schema(tags=['Vehículos'], description='Listado de vehículos')
@extend_schema_view(
    retrieve=extend_schema(summary='Detalle de vehículo', description='Detalle de un vehículo'),
    create=extend_schema(summary='Crear vehículo', description='Crear un vehículo'),
    update=extend_schema(summary='Actualizar vehículo', description='Actualizar un vehículo'),
    partial_update=extend_schema(
        summary='Actualizar parcialmente vehículo', description='Actualizar parcialmente un vehículo'
    ),
    destroy=extend_schema(summary='Eliminar vehículo', description='Eliminar un vehículo'),
    list=extend_schema(summary='Listar vehículos', description='Listar todos los vehículos'),
)
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]
