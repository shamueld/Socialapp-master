from __future__ import unicode_literals

from django.shortcuts import render
# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages


from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404

from django.views import generic

from braces.views import SelectRelatedMixin

from . import models
from .models import Server, Application, EAI
from .forms import ServerForm, EAIForm, ApplicationForm

import requests

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here. 

# Server Views

def index(request):
    my_dict = {'Insert':"Hello, Welcome to Inventory"}
    return render(request,'cmdb/cmdb_index.html',context=my_dict)

class ServerList(SelectRelatedMixin,generic.ListView):    
    model = models.Server
    form_class = ServerForm
    select_related = ()

# class ApplicatonServers(generic.ListView):
#     model = models.Server
#     template_name = 'cmdb/app_server_list.html' 

#     def get_queryset(self):
#         try:
#             self.server_app = Application.objects.prefetch_related('apps').get(name__iexact=self.kwargs.get('name'))
#         except Application.DoesNotExiist:
#             raise Http404
#         else:
#             return self.server_app.servers.all()
        
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['server_app'] = self.server_app
#         context['name'] = self.server_app.name
#         return context

class ServerDetail(SelectRelatedMixin,generic.DetailView):
    model = models.Server
    form_class = ServerForm
    select_related = ()

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(user__username__iexact = self.kwargs.get('username'))

class CreateServer(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    model = models.Server
    form_class = ServerForm


class DeleteServer(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Server
    form_class = ServerForm
    select_related = ()
    success_url = reverse_lazy('cmdb:all')

    
    def delete(self,*args,**kwargs):
        messages.success(self.request,'Server Deleted')
        return super().delete(*args,**kwargs) 

# Application Views

class ApplicationList(SelectRelatedMixin,generic.ListView):    
    model = models.Application
    form_class = ApplicationForm
    select_related = ()

class ApplicationDetail(SelectRelatedMixin,generic.DetailView):
    model = models.Application
    form_class = ApplicationForm
    select_related = ()


class CreateApplication(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    model = models.Application
    form_class = ApplicationForm

class DeleteApplication(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Application
    form_class = ApplicationForm
    select_related = ()
    success_url = reverse_lazy('cmdb:all')

    
    def delete(self,*args,**kwargs):
        messages.success(self.request,'Application Deleted')
        return super().delete(*args,**kwargs) 


# EAI Views

class EAIList(SelectRelatedMixin,generic.ListView):    
    model = models.EAI
    form_class = EAIForm
    select_related = ()

class EAIDetail(SelectRelatedMixin,generic.DetailView):
    model = models.EAI
    select_related = ()
    form_class = EAIForm

class CreateEAI(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    model = models.EAI
    form_class = EAIForm

class DeleteEAI(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.EAI
    form_class = EAIForm
    select_related = ()
    success_url = reverse_lazy('cmdb:all')

    
    def delete(self,*args,**kwargs):
        messages.success(self.request,'EAI Deleted')
        return super().delete(*args,**kwargs) 

