from django_filters import rest_framework as filters
from .models import Candidates


class FilterCandidates(filters.FilterSet):
    class Meta:
        model = Candidates
        fields = [
            "name",
            "email",
            "cpf",
            "salary_claim",
            "immediate_availability",
            "age",
        ]
