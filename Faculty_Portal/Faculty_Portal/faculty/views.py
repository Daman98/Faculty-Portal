from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Faculty_Portal.faculty.forms import SignUpForm, InfoForm
from django.contrib.auth.models import User
raw_password=" "
@login_required
def home(request):
    return render(request, 'home.html')

def home_page_view(request):
    return render(request, 'home1.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('infopage')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def info(request):
    form = InfoForm()
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            userinfo = form.save(commit=False)
            # userinfo.user = user.objects.filter(id=request.user).first() 
            userinfo.user = request.user 
            userinfo.full_name = form.cleaned_data.get('full_name')
            userinfo.birth_date = form.cleaned_data.get('birth_date')
            userinfo.department = form.cleaned_data.get('department')
            #userinfo.profile.profile_picture = form.cleaned_data.get('profile_picture')
            userinfo.save()
            return redirect('home')
    else:
        form = InfoForm()
    return render(request, 'info.html', {'form': form})
