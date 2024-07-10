from rest_framework import status
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema_view
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from tickets.apps.cars.models import Car
from tickets.apps.civils.models import Civil
from tickets.apps.infringements.models import Infringement
from tickets.apps.infringements.api.serializers import InformerSerializer
from tickets.apps.infringements.api.serializers import InfringementSerializer
from tickets.apps.infringements.api.serializers import CarInfringementsSerializer
from tickets.apps.infringements.api.serializers import SearchInfringementSerializer


@extend_schema(tags=["Infracciones"])
@extend_schema_view(
    retrieve=extend_schema(summary="Detalle de infracción", description="Detalle de una infracción"),
    create=extend_schema(summary="Crear infracción", description="Crear una infracción"),
    destroy=extend_schema(summary="Eliminar infracción", description="Eliminar una infracción"),
    list=extend_schema(summary="Listar infracciones", description="Listar todas las infracciones"),
    generate_report=extend_schema(
        summary="Generar reporte",
        description="Generar reporte de infracciones de una persona, se tiene que pasar como argumento el correo electrónico",
    ),
    by_car=extend_schema(
        summary="Listar infracciones por vehículo",
        description="Devuelve una lista de infracciones pertenecientes a un vehículo específico.",
    ),
)
class InfringementView(viewsets.ModelViewSet):
    queryset = Infringement.objects.all()
    serializer_class = InfringementSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "delete"]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["car"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            infringement = serializer.save()
            return Response(self.get_serializer(infringement).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"], url_path="generate-report", permission_classes=[AllowAny])
    def generate_report(self, request):
        serializer = SearchInfringementSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]

        try:
            civil = Civil.objects.get(email=email)
            infringements = Infringement.objects.filter(car__owner=civil)
            serializer = InformerSerializer(infringements, many=True)
            return Response(serializer.data)
        except Civil.DoesNotExist:
            return Response({"error": "Persona no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=["get"], url_path="by-car/(?P<car_id>\d+)")
    def by_car(self, request, car_id=None):
        try:
            car = Car.objects.get(pk=car_id)
        except Car.DoesNotExist:
            return Response({"detail": "Vehículo no encontrado."}, status=status.HTTP_404_NOT_FOUND)

        infringements = Infringement.objects.filter(car=car)
        serializer = CarInfringementsSerializer({"car": car, "infringements": infringements})
        return Response(serializer.data)

