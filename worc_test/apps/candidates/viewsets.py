from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from django.db.models import Q

from .models import Candidates
from .serializers import CandidatesSerializer
from .filters import FilterCandidates


class CandidatesManagerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Candidates.objects.all()
    serializer_class = CandidatesSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = FilterCandidates


class CandidatesViewSet(viewsets.GenericViewSet):
    def post(self, request, *args, **kwargs):
        serializer = CandidatesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )
