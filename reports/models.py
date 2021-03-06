from django.db import models
from profiles.models import ReportsUser
from django import forms
from datetime import datetime 

class Report(models.Model):
	REPORT_STATUS = (
		(u'R', u'Reportado'),
		(u'P', u'Procesando'),
		(u'C', u'Completado'),
		)
	REPORT_TYPES = (
		(u'A', u'Averia'),
		(u'T', u'Tubo Roto'),
		(u'F', u'Fuga de Agua'),
		(u'E', u'Otros')
		)
	description = models.CharField(max_length=60)
	date = models.DateField(default=datetime.now)
	rep_type = models.CharField(max_length=1, choices= REPORT_TYPES, default='A' )
	status = models.CharField(max_length=1, choices= REPORT_STATUS, default='R')
	status_comment = models.CharField(max_length=60, default='Reported')
	latitude = models.FloatField()
	longitude = models.FloatField()
	count = models.IntegerField(default=1)
	email = models.EmailField()
	photo_path = models.ImageField(upload_to="./report_photos", blank=True, null=True, default='./report_photos/drop_logo.png', verbose_name="Upload Foto")
	assign_to =  models.ForeignKey(ReportsUser, blank=True, null=True, on_delete=models.SET_NULL)

	def __unicode__(self):
		return self.description

class Polygon(models.Model):
	name = models.CharField(max_length=60)
	polygon = models.TextField()

	def __unicode__(self):
		return self.name
    
class AssignForm(forms.Form):
    Assign_to = forms.ModelChoiceField(queryset=ReportsUser.objects.filter(is_employee=True))

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['status', 'status_comment']

class ReportCreateForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['description','rep_type','latitude','longitude','email', 'photo_path',]
