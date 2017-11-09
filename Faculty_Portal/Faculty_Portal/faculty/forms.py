from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Faculty_Portal.faculty.models import Profile
from django.db import models
class SignUpForm(UserCreationForm):
   #birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

class InfoForm(forms.ModelForm):

   	class Meta:
   		model = Profile
		# fields = ('full_name','birth_date','department')
		fields = ('full_name','birth_date', 'department',)

	# full_name = forms.CharField()
 #   	birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
 #   	department = forms.CharField()
 #  	profile_picture = forms.ImageField()
