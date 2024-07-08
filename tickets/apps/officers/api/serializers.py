from rest_framework import serializers

from tickets.apps.officers.models import Officer


class OfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officer
        fields = ['id', 'email', 'fullname', 'badge_number']
