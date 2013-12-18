from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from reports.models import Report, Polygon
from snippets.serializers import ReportSerializer, ListSerializer
from shapely.geometry import shape, Point
import json
import urllib2
from django.http import HttpResponse

@api_view(['GET', 'POST'])
def report_list(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        reports = Report.objects.all()
        serializer = ListSerializer(reports, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReportSerializer(data=request.DATA)
        print request.DATA
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def report_detail(request, pk):
            
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
    try:
        poly = Polygon.objects.get(name=pueblo)
    except Polygon.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        sh = shape(json.loads(poly.polygon))
        report_list = Report.objects.all()
        result = []
        for point in report_list:
            x = Point(point.latitude, point.longitude)
            print x
            if Point(point.latitude, point.longitude).within(sh):
                result.append(point)
                

        serializer = ReportSerializer(result, many=True)
        print result

        return Response(serializer.data)

def mobile_news(request):
    f = urllib2.urlopen('http://136.145.188.31:8000/api/?format=json')
    data = f.read()
    return HttpResponse('{ "News": ' + data + "}")
















