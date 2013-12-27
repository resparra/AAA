#from django.http import HttpResponse
from reports.models import Report, ReportCreateForm
from django.shortcuts import render


def index(request):
	report_list = Report.objects.all().order_by('-id')
	context = {'report_list' : report_list }

	return render(request, 'reports/index.html', context)

def map_list(request):
	report_list = Report.objects.all().order_by('-id')
	context = {'report_list' : report_list }

	return render(request, 'reports/mobile_map.html', context)

def create_rep(request):
	report_list = Report.objects.all().order_by('-id')
	form = ReportCreateForm()
	context = {'report_list' : report_list, 'form': form }

	if request.method == 'POST':
		report_form = ReportCreateForm(request.POST, request.FILES)

		if report_form.is_valid():
			if request.FILES:
				report_form.photo_path = request.FILES['photo_path']
			report_form.save()
			return render(request, 'reports/create_reports.html', context)
		else :
			error = report_form.errors
			context = {'report_list' : report_list, 'form': form, 'error': error }
			return render(request, 'reports/create_reports.html', context)
	else :
		return render(request, 'reports/create_reports.html', context)	