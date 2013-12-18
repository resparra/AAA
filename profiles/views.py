# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from reports.models import Report, AssignForm, ReportForm
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from profiles.forms import ReportsUserForm, ReportsUser
from datetime import datetime
from django.core.mail import send_mail 

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
	if request.method == 'POST':
		form = ReportForm(request.POST)
		report = Report.objects.get(pk=form.data['id'])
		report.assign_to = ReportsUser.objects.get(pk=form.data['Assign_to'])
		print report
		report.save()


	form = AssignForm()
	report_list = Report.objects.filter(assign_to__isnull=True).order_by('-id')
	context = {'report_list' : report_list, 'form' : form }

	return render(request, 'profiles/supervisor.html', context)

@permission_required('profiles.employee_permission')
def employee_view(request):
	error = False
	if request.method == 'POST':
		form = ReportForm(request.POST)
		if not form.data['status'] == "" and not form.data['status_comment'] == "":
			report = Report.objects.get(pk=form.data['id'])
			report.status = form.data['status']
			report.status_comment = form.data['status_comment']+" ("+str(datetime.now().date())+")" 
			report.save()

			message = "Update on your report:\n Comment: %s." %report.status_comment

			send_mail('Report update' , message, 'aaa.reports.news@gmail.com',
    			[report.email], fail_silently=False)



		else:
			error = True

	user = request.user
	form = ReportForm()
	report_list = Report.objects.filter(assign_to = user.id).order_by('-id')
	report_completed = report_list.filter(status='C')
	print report_completed
	if error:
		context = {'report_list' : report_list, 'form': form, 'error': error }
	else:
		context = {'report_list' : report_list, 'form': form }

	return render(request, 'profiles/employee.html', context)

def register(request):
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
                user.set_password(request.POST['password'])
                user.save()
                registered = True
                        # Invalid form or forms - mistakes or something else?
                        # # Print problems to the terminal.
                        # # They'll also be shown to the user.
                        # 
                # send mail
                send_mail('Thanks for your registration ', user.name + ',\n Thanks for registering in AAA reports application' ,'aaa.reports.news@gmail.com',
    			[user.email], fail_silently=False)
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



