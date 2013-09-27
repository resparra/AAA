from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from reports.models import Report
from snippets.serializers import ReportSerializer, ListSerializer


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
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def report_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
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



