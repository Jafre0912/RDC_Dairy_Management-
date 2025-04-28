from rest_framework import serializers
from .models import Cattle, Report

class CattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cattle
        fields = ['id', 'name', 'age', 'milk_production']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'title', 'content', 'created_at']