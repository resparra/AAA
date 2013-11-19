from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from reports.models import Report, Polygon
from snippets.serializers import ReportSerializer, ListSerializer
from shapely.geometry import shape, Point
import json


@api_view(['GET', 'POST'])
def report_list(request):
    """
    List all reports, or create a new one.
    """
    if request.method == 'GET':
        reports = Report.objects.all()
        serializer = ListSerializer(reports, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReportSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def report_detail(request, pk):
    """
    Specific Report Infomation
    """       
    try:
        report = Report.objects.get(pk=pk)
    except Report.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReportSerializer(report)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReportSerializer(report, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def report_location(request, pueblo):
    """
    List all reports within a polygon.
    """
    try:
        poly = Polygon.objects.get(name=pueblo)
    except Polygon.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        sh = shape(json.loads(poly.polygon))
        report_list = Report.objects.all()
        result = []

        for point in report_list:
            if Point(point.longitude,point.latitude).within(sh):
                result.append(point)
                

        serializer = ListSerializer(result, many=True)
        print result

        return Response(serializer.data)
















