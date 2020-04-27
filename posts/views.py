# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages


from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404

from django.views import generic

from braces.views import SelectRelatedMixin

from . import models
from .forms import CommentForm

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

def index(request):
    my_dict = {'Insert':"Hello, I am inserted from Django tempate tags"}
    return render(request,'posts/index.html',context=my_dict)

class PostList(SelectRelatedMixin,generic.ListView):    
    model = models.Post
    select_related = ('user', 'group')

class UserPosts(generic.ListView):
    model = models.Post
    template_name = 'posts/user_list.html' 

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExiist:
            raise Http404
        else:
            return self.post_user.posts.all()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context

class PostDetail(SelectRelatedMixin,generic.DetailView):
    model = models.Post
    select_related = ('user','group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact = self.kwargs.get('username'))

class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('message', 'group')
    model = models.Post

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ('user','group')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__id = self.request.user.id)
    
    def delete(self,*args,**kwargs):
        messages.success(self.request,'Post Deleted')
        return super().delete(*args,**kwargs) 

def AddComment(request, username, pk):
    post = get_object_or_404(models.Post, pk=pk)
    user = get_object_or_404(User, username=username)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = user
            comment.save() 
            return redirect('posts:single', username=user.username, pk=post.pk)
        
    else:
        form = CommentForm()
    
    return render(request, 'posts/post_detail.html', {'form': form, 'user': user, 'post': post})