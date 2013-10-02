from django.db import models

class Report(models.Model):
	REPORT_STATUS = (
		('R', 'Reportado'),
		('P', 'Procesando'),
		('C', 'Completado'),
		)
	REPORT_TYPES = (
		('T', 'Tubo Roto'),
		('F', 'Fuga de Agua'),
		('E', 'Otros')
		)
	description = models.CharField(max_length=60)
	date = models.DateField(auto_now=True)
	rep_type = models.CharField(max_length=1, choices= REPORT_TYPES)
	status = models.CharField(max_length=1, choices= REPORT_STATUS)
	status_comment = models.CharField(max_length=60)
	latitude = models.FloatField()
	longitude = models.FloatField()
	count = models.IntegerField(default=1)
	email = models.EmailField()
	photo_path = models.ImageField(upload_to="./report_photos", blank=True, null=True, default='./report_photos/drop_logo.png')

	def __unicode__(self):
		return self.description
    
    
