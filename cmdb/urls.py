from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'cmdb'

urlpatterns = [ 
    url(r'^index/$', views.index, name='index'),
    # Servers
    url(r'^servers$', views.ServerList.as_view(), name='server_all'),
    url(r'^new_server/$', views.CreateServer.as_view(), name='create_server'),
         # url(r'^(?P<name>[-\w]+)/$', views.ApplicatonServers.as_view(), name='for_app'),
    url(r'^server/(?P<pk>\d+)/$', views.ServerDetail.as_view(), name='single_server'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteServer.as_view(), name='delete_server'),
    # Apps
    url(r'^apps$', views.ApplicationList.as_view(), name='app_all'),
    url(r'^new_app/$', views.CreateApplication.as_view(), name='create_app'),
    url(r'app/(?P<pk>\d+)/$', views.ApplicationDetail.as_view(), name='single_app'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteApplication.as_view(), name='delete_app'),
    # EAIs
    url(r'^eais$', views.EAIList.as_view(), name='eai_all'),
    url(r'^new_eai/$', views.CreateEAI.as_view(), name='create_eai'),
    url(r'eai/(?P<pk>\d+)/$', views.EAIDetail.as_view(), name='single_eai'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteEAI.as_view(), name='delete_eai'),
]
