from rest_framework import serializers

from tickets.apps.cars.models import Car
from tickets.apps.civils.models import Civil
from tickets.apps.civils.api.serializers import CivilSerializer


class CarSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=Civil.objects.all(), write_only=True)

    class Meta:
        model = Car
        fields = ['patent_plate', 'brand', 'color', 'owner']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['owner'] = CivilSerializer(instance.owner).data
        return representation
