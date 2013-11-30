# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from reports.models import Report, AssignForm, ReportForm
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
	form = AssignForm()
	report_list = Report.objects.filter(assign_to__isnull=True).order_by('-id')
	context = {'report_list' : report_list, 'form' : form }

	return render(request, 'profiles/supervisor.html', context)

@permission_required('profiles.employee_permission')
def employee_view(request):
	user = request.user
	report_list = Report.objects.filter(assign_to = user.id).order_by('-id')
	context = {'report_list' : report_list, 'form': form }
	return render(request, 'profiles/employee.html', context)




