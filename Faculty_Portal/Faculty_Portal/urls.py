"""Faculty_Portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from Faculty_Portal.faculty import views as core_views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup_view, name='sign'),
    url(r'^signup/done/$', core_views.signup, name='signup'), 
    url(r'^main/$', core_views.home_page_view),
    url(r'^myprofile/$', core_views.my_profile , name='my_profile'),
    url(r'^publication/$', core_views.publication_list , name='publication_list'),
    url(r'^education/$', core_views.education_list , name='education_list'),
    url(r'^research/$', core_views.research_list , name='research_list'),
    url(r'^project/$', core_views.project_list, name='project_list'),
    url(r'^course/active/$', core_views.course_list_active, name='course_list_active'),
    url(r'^course/inactive/$', core_views.course_list_inactive, name='course_list_inactive'),
     url(r'^course/active/(?P<part_id>[0-9]+)/$', core_views.course_delete_active, name='course_delete_active'),
     url(r'^course/inactive/(?P<part_id>[0-9]+)/$', core_views.course_delete_inactive, name='course_delete_inactive'),
     url(r'^publication/(?P<part_id>[0-9]+)/$', core_views.publication_delete, name='publication_delete'),
     url(r'^research/(?P<part_id>[0-9]+)/$', core_views.research_delete, name='research_delete'),
     url(r'^education/(?P<part_id>[0-9]+)/$', core_views.education_delete, name='education_delete'),
     url(r'^project/(?P<part_id>[0-9]+)/$', core_views.project_delete, name='project_delete'),
     url(r'^course/change_status/(?P<part_id>[0-9]+)/$', core_views.change_course_status, name='change_course_status'),
    url(r'^honor/$', core_views.honor_list, name='honor_list'),
     url(r'^honor/(?P<part_id>[0-9]+)/$', core_views.honor_delete, name='honor_delete'),
     url(r'^temp/$',TemplateView.as_view(template_name='home2.html'), name='slides'),
     url(r'^photos/', include('Faculty_Portal.faculty.urls', namespace='photos')),
    # url(r'^project/new/$', core_views.project_new, name='project_new'),
     url(r'^search/$', core_views.search_que , name='search'),
    url(r'^search/(?P<username>[\w.@+-]+)/$', core_views.prof_page , name='prof_page'),
     url(r'^email/$', core_views.email , name='email'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
