from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, InfoForm
from django.contrib.auth.models import User
from .models import project, publication, course, honor, Profile, education, research
from .forms import ProjectForm, PublicationForm, CourseForm, HonorForm, SearchForm, EducationForm, ResearchForm
# from .crawler import update
import time

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View

from .forms import PhotoForm, UpdateForm
from .models import Photo

from django.shortcuts import get_object_or_404
from django.db.models import Q
from bs4 import BeautifulSoup
import urllib.request

import re

def email(request):
    f = open("Faculty_Portal/faculty/templates/test.txt","r") 
    myList = []
    for line in f:
        myList.append(line)
    l = myList[3].split('"')[1::2];
    print(l[0])
    qs = Profile.objects.get(user=request.user)
    qs.title=l[0]
    qs.save()
    f.close()
    return redirect('/myprofile')

def update(request, soup):
    # print(url)
    # dic = {}
    # res = []
    # pro_res = []
    # r  = requests.get(url)
    # data = r.content
    # # data = urllib.request.urlopen(url).read()
    # soup = BeautifulSoup(str(data),'lxml')
    print("daman")
    main = soup.find("div", {"id": "fh5co-main"}, {"style": "text-align: left;"})
    ed = main.findAll("p")
    c = 13
    for a in ed:
        if 6 < c < 10:
            degree = a.text.split(',')
            sab = degree[0].split('\\n\\t\\t\\t')
            print(degree)
            print(sab)
            e = education(education_of=request.user)

            e.degree = sab[0]
            e.left= ""
            e.subject = sab[1]
            e.joined = degree[2]
            e.college = degree[1]
            e.save()
        c -= 1


raw_password = " "


@login_required
def home(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        print("bbbbb")
        if form.is_valid():
            print("aaaa")
            url = form.cleaned_data['update']
            print(url)
            # data = requests.get(url)
            # print("aagya")
            # data = data.content
            data = urllib.request.urlopen(url).read()
            #print(data)
            soup = BeautifulSoup(str(data), "lxml")
            update(request, soup)
        return redirect('/')
    else:
        print("aasdad")
        return render(request, 'index.html')


def home_page_view(request):
    return render(request, 'home1.html')


def signup_view(request):
    return render(request, 'signup.html')


def signup(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        raw_password1 = form.cleaned_data['password1']
        raw_password2 = form.cleaned_data['password2']
        # use=Profile()
        # use.user=username
        if raw_password1 == raw_password2:
            user.set_password(raw_password1)
            user.save()
            user = authenticate(username=username, password=raw_password1)
            login(request, user)
            return redirect('my_profile')
    else:
        return render(request, 'signup.html', {'form': form})


def my_profile(request):
    #user = User.objects.get(username=username,password=password)
    #form = InfoForm()
    if request.method == 'POST':
        form = InfoForm(request.POST,request.FILES)
        if form.is_valid():
            #userinfo = form.save(commit=False)
            # userinfo.user = user.objects.filter(id=request.user).first() 
            # userinfo.id=request.id
            a = Profile.objects.filter(user=request.user)
            if a.count()==0 :
                userinfo=form.save(commit=False)
                userinfo.user=request.user 
            else:
                userinfo=Profile.objects.get(user=request.user)
                

            
            userinfo.full_name = form.cleaned_data.get('full_name')
            userinfo.birth_date = form.cleaned_data.get('birth_date')
            
            #dropdown returns index so get dept from dictionary made of choices
            index = form.cleaned_data.get('department')
            userinfo.department = dict(form.fields['department'].choices)[index]

            index1 = form.cleaned_data.get('title')
            userinfo.title = dict(form.fields['title'].choices)[index1]
            
            userinfo.phone = form.cleaned_data.get('phone')
            userinfo.room= form.cleaned_data.get('room')

            temp=userinfo.profile_picture
            userinfo.profile_picture = form.cleaned_data.get('profile_picture')

            if len(request.FILES)==0 and a.count()!=0:
                userinfo.profile_picture = temp

            userinfo.save()
            return redirect('home')
    else:
        form = InfoForm()
        b = Profile.objects.filter(user=request.user)
        if b.count()!=0 :
            a = Profile.objects.get(user=request.user)
            form.fields['full_name'].initial=a.full_name
            form.fields['birth_date'].initial=a.birth_date
            form.fields['phone'].initial=a.phone
            form.fields['room'].initial=a.room
            form.fields['profile_picture'].initial=a.profile_picture

            start=0
            d=dict(form.fields['department'].choices)
            for x,y in d.items():
                if y==a.department:
                    start=x

            form.fields['department'].initial=start

            star=0
            di=dict(form.fields['title'].choices)
            for x,y in di.items():
                if y==a.title:
                    star=x

            form.fields['title'].initial=star
    return render(request, 'myprofile.html', {'form': form})


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()  # load the profile instance created by the signal
#             user.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password=raw_password)
#             login(request, user)
#             return redirect('infopage')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})

# def info(request):
#     form = InfoForm()
#     if request.method == 'POST':
#         form = InfoForm(request.POST,request.FILES)
#         if form.is_valid():
#             userinfo = form.save(commit=False)
#             # userinfo.user = user.objects.filter(id=request.user).first() 
#             userinfo.user = request.user 
#             userinfo.full_name = form.cleaned_data.get('full_name')
#             userinfo.birth_date = form.cleaned_data.get('birth_date')
#             #dropdown returns index so get dept from dictionary made of choices
#             index = form.cleaned_data.get('department')
#             userinfo.department = dict(form.fields['department'].choices)[index]

#             index1 = form.cleaned_data.get('title')
#             userinfo.title = dict(form.fields['title'].choices)[index1]

#             userinfo.phone = form.cleaned_data.get('phone')
#             userinfo.room= form.cleaned_data.get('room')

#             userinfo.profile_picture = form.cleaned_data.get('profile_picture')
#             userinfo.save()
#             return redirect('home')
#     else:
#         form = InfoForm()
#     return render(request, 'myprofile.html', {'form': form})

def publication_list(request):
    if request.method == "POST":
        form = PublicationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.publication_by = request.user
            post.save()
            return redirect('/publication/')
    else:
        form = PublicationForm()
    publications = publication.objects.filter(publication_by=request.user)
    return render(request, 'publications.html', {'publication': publications, 'form': form})


def publication_delete(request, part_id=None):
    obj = publication.objects.filter(id=part_id, publication_by=request.user)
    obj.delete()
    return redirect('/publication/')


def education_list(request):
    if request.method == "POST":
        form = EducationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.education_of = request.user
            post.save()
            return redirect('/education/')
    else:
        form = EducationForm()
    educations = education.objects.filter(education_of=request.user)
    return render(request, 'educations.html', {'education': educations, 'form': form})


def education_delete(request, part_id=None):
    obj = education.objects.filter(id=part_id, education_of=request.user)
    obj.delete()
    return redirect('/education/')


def research_list(request):
    if request.method == "POST":
        form = ResearchForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.res_of = request.user
            post.save()
            return redirect('/research/')
    else:
        form = ResearchForm()
    researchs = research.objects.filter(res_of=request.user)
    return render(request, 'researchs.html', {'research': researchs, 'form': form})


def research_delete(request, part_id=None):
    obj = research.objects.filter(id=part_id, res_of=request.user)
    obj.delete()
    return redirect('/research/')


def project_list(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.project_by = request.user
            post.save()
            return redirect('/project/')
    else:
        form = ProjectForm()
    projects = project.objects.filter(project_by=request.user)
    return render(request, 'projects.html', {'project': projects, 'form': form})


def project_delete(request, part_id=None):
    obj = project.objects.filter(id=part_id, project_by=request.user)
    obj.delete()
    return redirect('/project/')


def course_list_active(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.course_by = request.user
            post.save()
            return redirect('/course/active/')
    else:
        form = CourseForm()
    courses = course.objects.filter(course_by=request.user, course_active=True)
    return render(request, 'courseactive.html', {'course': courses, 'form': form})


def course_list_inactive(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.course_by = request.user
            post.save()
            return redirect('/course/inactive/')
    else:
        form = CourseForm()
    courses = course.objects.filter(course_by=request.user, course_active=False)
    return render(request, 'courseinactive.html', {'course': courses, 'form': form})


def course_delete_active(request, part_id=None):
    obj = course.objects.filter(id=part_id, course_by=request.user)
    obj.delete()
    return redirect('/course/active/')


def course_delete_inactive(request, part_id=None):
    obj = course.objects.filter(id=part_id, course_by=request.user)
    obj.delete()
    return redirect('/course/inactive/')


def change_course_status(request, part_id=None):
    obj = course.objects.get(id=part_id, course_by=request.user)
    obj.course_active = False
    obj.save()
    return redirect('/course/active/')


def honor_list(request):
    if request.method == "POST":
        form = HonorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.honor_for = request.user
            post.save()
            return redirect('/honor/')
    else:
        form = HonorForm()
    honors = honor.objects.filter(honor_for=request.user)
    return render(request, 'honors.html', {'honor': honors, 'form': form})


def honor_delete(request, part_id=None):
    obj = honor.objects.filter(id=part_id, honor_for=request.user)
    obj.delete()
    return redirect('/honor/')


class BasicUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.filter(slides_by=request.user)
        return render(self.request, 'basic_upload/index2.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.slides_by = request.user
            photo.title = photo.file.name
            photo.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


# def clear_database(request):
#     for photo in Photo.objects.all():
#         if photo.slides_by == request.user:
#             photo.file.delete()
#             photo.delete()
#     return redirect(request.POST.get('next'))


def clear_database(request, file_id=None):
    # for photo in Photo.objects.all():
    #     if photo.slides_by == request.user:
    #         if photo.id == file_id:
    #             photo.file.delete()
    #             photo.delete()
    de = Photo.objects.get(id=file_id, slides_by=request.user)
    de.file.delete()
    de.delete()
    return redirect('/photos/basic-upload')


def search_que(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query_name = form.cleaned_data['search']
            qs = Profile.objects.all()
            for term in query_name.split():
                qs = qs.filter(Q(full_name__icontains=term))
                return render(request, 'search.html', {'q': qs})
    else:
        form = SearchForm()
        return render(request, 'search.html')


def prof_page(request, username=None):
    qs = get_object_or_404(Profile, user__username=username)
    proj = project.objects.filter(project_by__username=username)
    edu = education.objects.filter(education_of__username=username)
    res = research.objects.filter(res_of__username=username)
    couac = course.objects.filter(course_by__username=username, course_active=True)
    couinac = course.objects.filter(course_by__username=username, course_active=False)
    publ = publication.objects.filter(publication_by__username=username)
    award = honor.objects.filter(honor_for__username=username, honor_type='Award')
    ach = honor.objects.filter(honor_for__username=username, honor_type='Achievement')
    oth = honor.objects.filter(honor_for__username=username, honor_type='Others')
    slide = Photo.objects.filter(slides_by__username=username)
    return render(request, 'response.html',
                  {'q': qs, 'proj': proj, 'edu': edu, 'res': res, 'couac': couac, 'couinac': couinac, 'publ': publ,
                   'award': award, 'ach': ach, 'oth': oth, 'slide': slide})
