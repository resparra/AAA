# profiles/models.py
from django.db import models
from django.contrib.auth.models import (
	BaseUserManager,
	AbstractBaseUser,
	PermissionsMixin)

class ReportsUserManager(BaseUserManager):

	def create_user(self,email,name,last_name,password=None):
		
		"""Creates and saves a user with given email,name,last_name, and password."""

		if not email:
			msg = "Users must have an email address"
			raise ValueError(msg)

		if not name:
			msg = "Users must have an name"
			raise ValueError(msg)

		if not last_name:
			msg = "Users must have an lastname"
			raise ValueError(msg)

		user = self.model(
			email=ReportsUserManager.normalize_email(email),
			name=name,
			last_name=last_name,
			)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,email,name,last_name,password):
		"""Creates and Saves superuser with given email,name,last_name and password"""

		user= self.create_user(email,name=name,last_name=last_name,password=password)

		user.is_superuser = True
		user.is_supervisor = True
		user.is_employee = True
		user.is_staff = True
		user.save(using=self._db)
		return user

	def create_supervisor(self,email,name,last_name,password):
		"""Creates and Saves employee with given email,name,last_name and password"""
		user = self.create_user(email,name=name,last_name=last_name,password=password)

		user.is_superuser = False
		user.is_supervisor = True
		user.is_employee = False
		user.user_permissions.add('supervisor_permission')
		user.save(using=self._db)
		return user

	def create_employee(self,email,name,last_name,password):
		"""Creates and Saves employee with given email,name,last_name and password"""
		user = self.create_user(email,name=name,last_name=last_name,password=password)

		user.is_superuser = False
		user.is_supervisor = False
		user.is_employee = True
		user.user_permissions.add('employee_permission')
		user.save(using=self._db)
		return user

	def create_client(self,email,name,last_name,password):
		"""Creates and Saves client with given email,name,last_name and password"""
		user = self.create_user(email,name=name,last_name=last_name,password=password)

		user.is_superuser = False
		user.save(using=self._db)
		return user

	def __unicode__(self):
		return self.user

USERNAME_FIELD = "email"
REQUIRED_FIELDS = ["name","last_name"]

class ReportsUser(AbstractBaseUser,PermissionsMixin):
	"""Inherits from both the AbastractBaseUser and PermissionsMixin"""

	email= models.EmailField(
		verbose_name="email adress",
		max_length=255,
		unique=True,
		db_index=True,
		)
	name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=15)

	USERNAME_FIELD = USERNAME_FIELD
	REQUIRED_FIELDS = REQUIRED_FIELDS

	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_supervisor = models.BooleanField(default=False)
	is_employee = models.BooleanField(default=False)

	objects = ReportsUserManager()

	def get_fullname(self):
		# The user is identified by their email
		# name and lastname
		return "%s %s email %s" % (self.name,self.last_name,self.email)

	def get_short_name(self):
		#The user is identified by their email
		return self.email

	def __unicode__(self):
		return self.email

	class Meta:
		permissions = (
			('employee_permission', 'See Employee view'),
			('supervisor_permission', 'See Supervisor view'),
		)




