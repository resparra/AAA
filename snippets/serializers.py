from rest_framework import serializers
from reports.models import Report


class ReportSerializer(serializers.ModelSerializer):
    photo_path = serializers.SerializerMethodField('get_file_url')

    class Meta:
        model = Report
        fields = ('id','description', 'date', 'rep_type', 'status', 'status_comment', 'latitude', 'longitude', 'count', 'email', 'photo_path',)

    def get_file_url(self, obj):
        if obj.photo_path :
            return obj.photo_path.url
        else :
            return ""

class ListSerializer(serializers.ModelSerializer):
    photo_path = serializers.SerializerMethodField('get_file_url')
    class Meta:
        model = Report
        fields = ('id','description', 'date', 'rep_type', 'status', 'latitude', 'longitude', 'status_comment', 'photo_path')

    def get_file_url(self, obj):
        if obj.photo_path :
            return obj.photo_path.url
        else :
            return ""


