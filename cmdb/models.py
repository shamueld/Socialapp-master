# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.conf import settings
from groups.models import Group

# Create your models here.
import misaka

from django.contrib.auth import get_user_model
User = get_user_model()


class Application(models.Model):
    name = models.CharField(max_length=32,unique=True)
    group = models.ManyToManyField(Group,related_name='apps',blank=True)

    def __str__(self):
        return self.name    

    def get_absolute_url(self):
        return reverse('cmdb:app_all') 

    class Meta:
        ordering = ['name']

class EAI(models.Model):
    eai_code = models.IntegerField(unique=True)
    app = models.ManyToManyField(Application, related_name='eais')

    def __str__(self):
        return str(self.eai_code)
    
    def get_absolute_url(self):
        return reverse('cmdb:eai_all',kwargs={'pk':self.pk})

    class Meta:
        ordering = ['eai_code']




class Server(models.Model):
    name = models.CharField(max_length=64,unique=True)

    osTypes = models.TextChoices('osTypes', 'linux windows aix')
    os_type = models.CharField(blank=True, choices=osTypes.choices, max_length=10)

    domainTypes = models.TextChoices('domainTypes', 'metnet met_intnet alicocorp')    
    domain= models.CharField(blank=True, choices=domainTypes.choices, max_length=10)

    envTypes = models.TextChoices('envTypes', 'Dev Int QA Prod DR Test')    
    environment = models.CharField(blank=True, choices=envTypes.choices, max_length=10)
    
    eai = models.ManyToManyField(EAI,related_name='servers',blank=True)
    app = models.ManyToManyField(Application,related_name='servers',blank=True)   
    

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        # message_html = misaka.html(self.message)
        super().save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse('cmdb:server_all',kwargs={'pk':self.pk})

    class Meta:
        ordering = ['name']