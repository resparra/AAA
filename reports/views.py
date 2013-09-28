#from django.http import HttpResponse
from reports.models import Report
from django.shortcuts import render

def index(request):
	report_list = Report.objects.all().order_by('-id')
	context = {'report_list' : report_list }

	return render(request, 'reports/index.html', context)