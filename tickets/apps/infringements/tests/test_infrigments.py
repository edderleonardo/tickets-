import uuid
from unittest.mock import MagicMock
from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from tickets.apps.cars.models import Car
from tickets.apps.civils.models import Civil
from tickets.apps.infringements.models import Infringement


User = get_user_model()


INFRINGEMENTS_URL = reverse('infringement-list')
INFRINGEMENTS_REPORT_URL = reverse('infringement-generate-report')


def create_user(email='user@example.com', password='testpass123'):
    """Create and return user."""
    return get_user_model().objects.create_user(email=email, password=password)


class PublicInfringementsTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_generate_report_invalid_email(self):
        """Test that generate_report returns empty list for a email that does not exist"""
        data = {'email': 'notexist@gmail.com'}
        res = self.client.post(INFRINGEMENTS_REPORT_URL, data, format='json')
        
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(res.data['error'], 'Persona no encontrada')


    def test_generate_report_valid_email(self):
        """Test that generate_report returns infringements for a email that exists"""
        civil = Civil.objects.create(fullname='John Doe', email='valid@example.com')
        car = Car.objects.create(patent_plate='ABC123', brand='Toyota', color='Blue', owner=civil)
        Infringement.objects.create(
            car=car, datetime='2023-01-01T00:00:00Z', comments='Estacionado en lugar prohibido', officer=create_user()
        )
        data = {'email': 'valid@example.com'}
        res = self.client.post(INFRINGEMENTS_REPORT_URL, data, format='json')

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['comments'], 'Estacionado en lugar prohibido')

    def test_create_infringement_no_authenticate(self):
        """Test that creating an infringement without authentication fails"""
        res = self.client.post(
            INFRINGEMENTS_URL,
            {'car': 1, 'datetime': '2023-01-01T00:00:00Z', 'comments': 'Estacionado en lugar prohibido'},
        )

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(res.data['detail'], 'Authentication credentials were not provided.')


class PrivateInfringementsTest(TestCase):
    def setUp(self):
        self.user = create_user()
        self.client = APIClient()

        # Genera un token para el usuario
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

        # Autentica el cliente con el token Bearer
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_create_infringement(self):
        """Test that creating an infringement with authentication succeeds"""
        civil = Civil.objects.create(email='user@example.com', fullname='John Doe')
        car = Car.objects.create(patent_plate='ABC123', brand='Toyota', color='Blue', owner=civil)

        INFRINGEMENTS_URL = reverse('infringement-list')

        res = self.client.post(
            INFRINGEMENTS_URL,
            {
                'patent_plate': car.patent_plate,
                'datetime': '2023-01-01T00:00:00Z',
                'comments': 'Estacionado en lugar prohibido',
            },
        )

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['comments'], 'Estacionado en lugar prohibido')
