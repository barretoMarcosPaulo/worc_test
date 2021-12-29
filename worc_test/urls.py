from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Worc Test API",
        default_version="v1",
        description="Technical test performed at worc",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/candidates/", include("worc_test.apps.candidates.urls")),
    path("api/reports/", include("worc_test.apps.reports.urls")),
    path("api/auth/", include("worc_test.apps.accounts.urls")),
    path(
        "",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
