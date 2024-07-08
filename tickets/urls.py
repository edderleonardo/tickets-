from django.urls import path
from django.urls import include
from django.contrib import admin
from drf_spectacular.utils import extend_schema
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularSwaggerView

from tickets.apps.auth.views import CustomTokenRefreshView
from tickets.apps.auth.views import CustomTokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('tickets.apps.officers.api.urls')),
    path('api/', include('tickets.apps.infringements.api.urls')),
    path('api/', include('tickets.apps.civils.api.urls')),
    path('api/', include('tickets.apps.cars.api.urls')),
]
