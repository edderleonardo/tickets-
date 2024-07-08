from django.db import models

from tickets.apps.cars.models import Car
from tickets.apps.core.models import TimeStampedModel
from tickets.apps.officers.models import Officer


class Infringement(TimeStampedModel):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='infringements')
    datetime = models.DateTimeField()
    comments = models.TextField()
    officer = models.ForeignKey(Officer, on_delete=models.CASCADE, related_name='infringements')

    def __str__(self):
        return f'{self.car} - {self.officer} - {self.comments}'
