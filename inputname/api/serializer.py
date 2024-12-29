from rest_framework import serializers
from .models import PerfTitle

class PerfTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfTitle
        fields = '__all__'