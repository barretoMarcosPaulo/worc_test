from rest_framework import serializers
from .models import Candidates


class CandidatesSerializer(serializers.ModelSerializer):
    def update(self, obj, validated_data):
        if validated_data.get("cpf", False):
            raise serializers.ValidationError("cpf field not editable")
        return obj

    class Meta:
        model = Candidates
        fields = "__all__"
