# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect
from reports.models import Report
from profiles.models import ReportsUser, ReportsUserManager
from profiles.forms import ReportsUserForm
from django.shortcuts import render, render_to_response
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
	user = request.user
	report_list = Report.objects.filter(assign_to = user.id).order_by('-id')
	context = {'report_list' : report_list }
	return render(request, 'profiles/employee.html', context)

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = ReportsUserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
        	user = user_form.save()
        	user.set_password(user.password)
        	user.save()
        	registered = True
			# Invalid form or forms - mistakes or something else?
			# # Print problems to the terminal.
			# # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = ReportsUserForm()

    # Render the template depending on the context.
    return render_to_response(
            'accounts/register.html',
            {'user_form': user_form,'registered': registered},
            context)



