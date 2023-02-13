from rest_framework import serializers
from .models import ApprData

class ApprDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprData
        fields = '__all__'