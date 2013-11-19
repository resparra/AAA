# Create your views here.
# from reports.models import Report
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
#from django.shortcuts import render

def index_login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
	    if user.is_active:
	        login(request, user)
	        return HttpResponseRedirect("/admin/")
	    else:
	        return HttpResponseRedirect("/")
	else:
	    return HttpResponseRedirect("/")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
