# profiles/models.py
from django.db import models
from django.contrib.auth.models import (
	BaseUserManager,
	AbastractBaseUser,
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

	user.is_admin = True
	user.is_staff = True
	user.is_superuser = True
	user.save(using=self._db)
	return user

def create_employee(self,email,name,last_name,password):
	"""Creates and Saves employee with given email,name,last_name and password"""
	user = self.create_user(email,name=name,last_name=last_name,password=password)

	user.is_admin = True
	user.is_staff = True
	user.is_superuser = False
	user.save(using=self._db)
	return user

def create_client(self,email,name,last_name,password):
	"""Creates and Saves client with given email,name,last_name and password"""
	user = self.create_user(email,name=name,last_name=last_name,password=password)

	user.is_admin = False
	user.is_staff = False
	user.is_superuser = False
	user.save(using=self._db)
	return user





