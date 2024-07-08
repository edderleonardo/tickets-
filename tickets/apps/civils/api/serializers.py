from rest_framework import serializers

from tickets.apps.civils.models import Civil


class CivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil
        fields = ['id', 'fullname', 'email']
