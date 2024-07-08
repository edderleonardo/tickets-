from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView


@extend_schema(tags=['auth'])
class CustomTokenObtainPairView(TokenObtainPairView):
    @extend_schema(description='Obtiene un par de tokens JWT (access y refresh)', operation_id='token_obtain_pair')
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


@extend_schema(tags=['auth'])
class CustomTokenRefreshView(TokenRefreshView):
    @extend_schema(description='Refresca un token JWT de acceso', operation_id='token_refresh')
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
