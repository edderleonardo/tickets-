from rest_framework import serializers

from tickets.apps.cars.models import Car
from tickets.apps.civils.models import Civil
from tickets.apps.civils.api.serializers import CivilSerializer


class CarSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=Civil.objects.all())

    class Meta:
        model = Car
        fields = ['id', 'patent_plate', 'brand', 'color', 'owner']

class CarDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['id', 'patent_plate', 'brand', 'color']

    
class OwnerCarsSerializer(serializers.ModelSerializer):
    cars = CarDetailSerializer(many=True, read_only=True)
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Civil
        fields = ['owner', 'cars']

    def get_owner(self, obj):
        return {'fullname': obj.fullname}
