from django import forms
from profiles.models import ReportsUser

class ReportsUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = ReportsUser
        fields = ('email','name','last_name')