from __future__ import unicode_literals
from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .choices import *


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=500)
    birth_date = models.DateField()
    department=models.CharField(max_length=10,choices=DEPT_CHOICES)
    profile_picture = models.ImageField(upload_to = 'faculty/Photos',null=True,default='faculty/Photos/2.jpg')
    title = models.CharField(max_length=50,choices=TITLE_CHOICES)
    phone = models.CharField(max_length=10)
    room = models.CharField(max_length=10)

class project(models.Model):
    project_by = models.ForeignKey('auth.User')
    project_name = models.CharField(max_length=200)
    pi = models.CharField(max_length=200)
    funding_agency = models.CharField(max_length=200)
    start_date=models.DateField(null=True, blank=True)
    end_date=models.DateField(null=True, blank=True)

    def __str__(self):
        return self.project_name

class publication(models.Model):
    publication_by = models.ForeignKey('auth.User')
    publication_name = models.CharField(max_length=200)
    coll = models.CharField(max_length=200, null=True)
    year=models.IntegerField(null=True, blank=True)
    other_info=models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.publication_name

class course(models.Model):
    course_by = models.ForeignKey('auth.User')
    course_code=models.CharField(max_length=10)
    course_name = models.CharField(max_length=200) 
    semester=models.CharField(max_length=20,choices=(('Even Semester',  'Even Semester'),('Odd Semester', 'Odd Semester')))
    session_start = models.IntegerField(null=True, blank=True)
    session_end = models.IntegerField(null=True, blank=True)
    course_active=models.BooleanField(default=True)

    def __str__(self):
        return self.course_code

class education(models.Model):
    education_of = models.ForeignKey('auth.User')
    degree = models.CharField(max_length=100,null=True)
    college=models.CharField(max_length=200,null=True)
    subject=models.CharField(max_length=100,null=True)
    joined=models.CharField(max_length=10,null=True)
    left=models.CharField(max_length=10,null=True, blank=True)

    def __str__(self):
        return self.degree

class research(models.Model):
    res_of = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class honor(models.Model):
    honor_for = models.ForeignKey('auth.User')
    honor_name =models.CharField(max_length=100)
    honor_from = models.CharField(max_length=25) 
    year = models.IntegerField(null=True, blank=True)
    honor_type=models.CharField(max_length=20,choices=(('Award',  'Award'),('Achievement', 'Achievement'),('Others', 'Others')))
    
    def __str__(self):
        return self.honor_name

class Photo(models.Model):
    slides_by = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='faculty/docs')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title





# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
