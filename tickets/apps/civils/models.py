from django.db import models

from tickets.apps.core.models import TimeStampedModel


class Civil(TimeStampedModel):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.fullname
