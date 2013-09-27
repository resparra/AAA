
from rest_framework import serializers
from reports.models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id','description', 'date', 'rep_type', 'status', 'status_comment', 'latitude', 'longitude', 'count', 'email', 'photo_path',)

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id','description', 'date', 'rep_type', 'status', 'latitude', 'longitude')