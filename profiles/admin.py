# profiles/admin.py

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import ReportsUser

class ReportsUserCreationForm(forms.ModelForm):
	""" A form for creating new users. Includes all the required fields, plus a repeated password"""
	password1 = forms.CharField(
		label="Password",
		widget=forms.PasswordInput)
	password2 = forms.CharField(
		label="Password confirmation",
		widget=forms.PasswordInput)

	class Meta:
		model = ReportsUser
		fields = (
			"email",
			"name",
			"last_name")

	def clean_password2(self):
		#Check that the two password 
		#entries match
		data = self.cleaned_data
		password1 = data.get("password1")
		password2 = data.get("password2")
		if password1 and password2 and password1 != password2:
			msg = "Passwords don't match"
			raise forms.ValidationError(msg)
		return password2

	def save(self, commit=True):
		#Save the provided password
		# in hashed format
		user = super(ReportsUserCreationForm, self).save(commit=False)

		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user

class ReportsUserChangeForm(forms.ModelForm):
	"""A form for updating users. Includes all the fields on the user, but replaces the password fields
	with admin"s password hash display field."""

	password = ReadOnlyPasswordHashField()

	class Meta:
		model = ReportsUser

	def clean_password(self):
		# Regardless of what the user provides, return the
		# initial value. This is done here, rather than on
		# the field, because the field does not have access
		# to the initial value
		return self.initial["password"]


class ReportsUserAdmin(UserAdmin):
	# Set the add/modify forms
	add_form = ReportsUserCreationForm
	form = ReportsUserChangeForm
	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User.
	list_display = ("email", "is_supervisor", "is_employee" ,"name", "last_name")
	list_filter = ("is_employee", "is_supervisor", "is_superuser", "is_active","groups")
	search_fields = ("email", "name", "last_name")
	ordering = ("email",)
	filter_horizontal = ("groups", "user_permissions",)
	fieldsets = (
		(None, {"fields": ("email", "password")}),
		("Personal info", {"fields": ("name", "last_name",)}),
		("Permissions", {"fields": ("is_active",
								"is_staff",
								"is_employee",
								"is_supervisor",
								"is_superuser",
								"groups",
								"user_permissions")}),
		("Important dates", {"fields": ("last_login",)}),
		)
	add_fieldsets = (
		(None, {
			"classes": ("wide",),
			"fields": ("email", "name", "last_name", "password1", "password2")}
		),
	)
# Register the new TwoScoopsUserAdmin

admin.site.register(ReportsUser, ReportsUserAdmin)
