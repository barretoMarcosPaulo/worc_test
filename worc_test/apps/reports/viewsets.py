from rest_framework import status, viewsets
from rest_framework.response import Response
from django.utils import timezone

from rest_framework.permissions import IsAuthenticated

from worc_test.apps.candidates.models import Candidates
from worc_test.apps.candidates.serializers import CandidatesSerializer


class AgeReportViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        <strong>Response samples:</strong><br>
        <pre>
        <code>
            {
                "youngerer": {
                    "id": 10,
                    "name": "Marcos Paulo",
                    "email": "marcosbra@gmail.com",
                    "cpf": "04846175324",
                    "age": 18,
                    "salary_claim": "12.50",
                    "immediate_availability": true
                },
                "older": {
                    "id": 11,
                    "name": "Joao Ferreira",
                    "email": "jao@gmail.com",
                    "cpf": "52186536080",
                    "age": 28,
                    "salary_claim": "2.50",
                    "immediate_availability": false
                },
                "average": 23
            }
        </code>
        </pre>
        """
        all_candidates = Candidates.objects.all()

        if all_candidates:
            older_candidate = Candidates.objects.latest("age")
            younger_candidate = Candidates.objects.earliest("age")

            datas = {
                "youngerer": CandidatesSerializer(younger_candidate).data,
                "older": CandidatesSerializer(older_candidate).data,
                "average": (younger_candidate.age + older_candidate.age) // 2,
            }

            return Response(
                datas,
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                [],
                status=status.HTTP_200_OK,
            )


class SalaryReportViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        """
        <strong>Response samples:</strong><br>
        <pre>
        <code>
            {
                "lowest": {
                    "id": 11,
                    "name": "Joao Ferreira",
                    "email": "jao@gmail.com",
                    "cpf": "52186536080",
                    "age": 28,
                    "salary_claim": "2.50",
                    "immediate_availability": false
                },
                "highest": {
                    "id": 10,
                    "name": "Marcos Paulo",
                    "email": "marcosbra@gmail.com",
                    "cpf": "04846175324",
                    "age": 18,
                    "salary_claim": "12.50",
                    "immediate_availability": true
                },
                "average": 7.5
            }
        </code>
        </pre>
        """
        all_candidates = Candidates.objects.all()

        if all_candidates:
            highest_salary_candidate = Candidates.objects.latest("salary_claim")
            lowest_salary_candidate = Candidates.objects.earliest("salary_claim")
            salary_sum = (
                highest_salary_candidate.salary_claim
                + lowest_salary_candidate.salary_claim
            )

            datas = {
                "lowest": CandidatesSerializer(lowest_salary_candidate).data,
                "highest": CandidatesSerializer(highest_salary_candidate).data,
                "average": salary_sum / 2,
            }

            return Response(
                datas,
                status=status.HTTP_200_OK,
            )

        else:
            return Response(
                [],
                status=status.HTTP_200_OK,
            )
