# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from reports.models import Report
from profiles.models import ReportsUser
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

def index_login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
	    if user.is_active:
	        login(request, user)
	        if user.is_superuser:
	        	return HttpResponseRedirect("/admin")
	        else:
	        	return HttpResponseRedirect("/")
	    else:
	        return HttpResponseRedirect("/")
	else:
	    return HttpResponseRedirect("/")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@permission_required('profiles.supervisor_permission')
def supervisor_view(request):
	employees = ReportsUser.objects.filter(is_employee=True)
	report_list = Report.objects.filter(assign_to__isnull=True).order_by('-id')
	context = {'report_list' : report_list, 'employees' : employees }

	return render(request, 'profiles/supervisor.html', context)

@permission_required('profiles.employee_permission')
def employee_view(request):
	report_list = Report.objects.all().order_by('-id')
	context = {'report_list' : report_list }
	return render(request, 'profiles/employee.html', context)




