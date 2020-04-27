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

class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts',blank=True,null=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts',blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.message
    
    def save(self,*args,**kwargs):
        message_html = misaka.html(self.message)
        super().save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,
                                                'pk':self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user','message']

class Comment(models.Model):
    message = models.TextField()
    post = models.ForeignKey(Post,related_name='comments',blank=True,null=True,on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='comments',blank=True,null=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.message       

    class Meta:
        ordering = ['-created_at']


