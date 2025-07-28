# alx_travel_app_0x01/alx_travel_app/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Schema view for Swagger/OpenAPI documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Travel App API",
        default_version='v1',
        description="API for managing travel listings and bookings.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@travelapp.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # API endpoints for listings and bookings
    path('api/', include('listings.urls')),
    # Swagger UI and ReDoc documentation paths
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

