from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from tickets.apps.cars.models import Car
from tickets.apps.infringements.models import Infringement


class InfringementSerializer(serializers.ModelSerializer):
    patent_plate = serializers.CharField(write_only=True)

    class Meta:
        model = Infringement
        fields = ['id', 'patent_plate', 'datetime', 'comments']
        read_only_fields = ['car', 'officer']

    def validate_patent_plate(self, value):
        if not value:
            raise serializers.ValidationError('patent_plate is required')
        try:
            Car.objects.get(patent_plate=value)
        except Car.DoesNotExist:
            raise serializers.ValidationError(f'No car found with patent plate: {value}')
        return value

    def create(self, validated_data):
        patent_plate = validated_data.pop('patent_plate')
        car = Car.objects.get(patent_plate=patent_plate)
        officer = self.context['request'].user
        return Infringement.objects.create(car=car, officer=officer, **validated_data)


class InformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infringement
        fields = ['id', 'car', 'datetime', 'comments']
        read_only_fields = ['car', 'officer']


class SearchInfringementSerializer(serializers.Serializer):
    email = serializers.EmailField() 