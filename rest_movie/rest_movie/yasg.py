from django.urls import path
from rest_framework import  permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


get_schema_view = get_schema_view(
    openapi.Info(
        title='Django Movie',
        default_version='v1',
        description='Test description',
        license=openapi.License(name= "BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns =[
    path('swagger(?P<format>\.json|\.yaml)', get_schema_view.without_ui(cache_timeout=0),name='schema=json'),
    path('swagger/', get_schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('redoc/', get_schema_view.with_ui('redoc',cache_timeout=0),name='schema-redoc'),

]