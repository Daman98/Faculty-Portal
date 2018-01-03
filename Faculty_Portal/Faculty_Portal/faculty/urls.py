from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^clear/$', views.clear_database, name='clear_database'),#url(r'^clear/$', views.clear_database, name='clear_database'),
    url(r'^basic-upload/$', views.BasicUploadView.as_view(), name='basic_upload'),
     url(r'^clear/(?P<file_id>[0-9]+)/$', views.clear_database, name='clear_file'),
]
