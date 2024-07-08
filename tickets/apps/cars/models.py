from django.db import models

from tickets.apps.core.models import TimeStampedModel
from tickets.apps.civils.models import Civil


class Car(TimeStampedModel):
    patent_plate = models.CharField(max_length=10)
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    owner = models.ForeignKey(Civil, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return f'{self.owner} - {self.patent_plate} - {self.brand} - {self.color}'
