from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Faculty_Portal.faculty.models import Profile
from django.db import models
import datetime
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm, Form
from django.forms import extras
from datetime import datetime
from .choices import *
from .models import project,Profile,publication,course,honor,Photo,education,research


date_range = 100    
this_year = datetime.now().year

class UpdateForm(forms.Form):
    update = forms.CharField(max_length=500)
    class Meta:
        fields = ('update')

class ProjectForm(forms.ModelForm):

    class Meta:
        model = project
        fields = ('project_name', 'pi','funding_agency','start_date','end_date')

class PublicationForm(forms.ModelForm):

    class Meta:
        model = publication
        fields = ('publication_name', 'coll','year','other_info')

class EducationForm(forms.ModelForm):

    class Meta:
        model = education
        fields = ('degree', 'subject','college','joined','left')

class ResearchForm(forms.ModelForm):

    class Meta:
        model = research
        fields = ('title',)

class CourseForm(forms.ModelForm):

    class Meta:
        model = course
        fields = ('course_code','course_name','semester','session_start','session_end','course_active')

class HonorForm(forms.ModelForm):

    class Meta:
        model = honor
        fields = ('honor_type','honor_name','honor_from','year')

class SignUpForm(UserCreationForm):
   #birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    password1=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

class InfoForm(forms.ModelForm):
    title= forms.ChoiceField(choices=TITLE_CHOICES, widget=forms.RadioSelect())
    department= forms.ChoiceField(choices = DEPT_CHOICES, required=True)
    birth_date= forms.DateField(widget=extras.SelectDateWidget(years=range(this_year - date_range, this_year)))


    class Meta:
        model = Profile
        fields = ('full_name', 'department', 'title', 'phone','room', 'profile_picture','birth_date',)

	# full_name = forms.CharField()
 #   	birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
 #   	department = forms.CharField()
 #  	profile_picture = forms.ImageField()

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('file', )


class SearchForm(forms.Form):
    search = forms.CharField(required=True)
    class Meta:
        fields = ('search')