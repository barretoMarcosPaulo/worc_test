from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CandidatesManagerViewSet, CandidatesViewSet

app_name = "candidates"

router = DefaultRouter()
router.register("manager", CandidatesManagerViewSet, basename="candidates")

urlpatterns = [
    path(
        "register/",
        CandidatesViewSet.as_view({"post": "post"}),
    ),
]

urlpatterns += router.urls
