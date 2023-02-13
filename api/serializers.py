from rest_framework.serializers import ModelSerializer
from .models import RawAppraisalData

class RawAppraisalDataSerializer(ModelSerializer):
    class Meta:
        model = RawAppraisalData
        fields = ['id', 'description']