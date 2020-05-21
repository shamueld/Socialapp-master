from django.views.generic import (ListView, DetailView, UpdateView, DeleteView,
                                    TemplateView, CreateView)

from posts.models import Post
from groups.models import Group
from django.contrib.auth.forms import AuthenticationForm
import requests
# response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=cary,us&APPID=e8a1bb91b6558e6f3ffd4086379d3527")
# geodata = response.json() 

from django.contrib.auth import get_user_model
User = get_user_model()

class BasePage(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = AuthenticationForm
        return context

def searchUser(uname):
    return User.objects.filter(username__startswith=uname)
    

class HomePage(TemplateView):
    template_name = 'index.html'


    def get_context_data(self, **kwargs):        
        searchUsers = []
        searchUsers = searchUser("sam")
        
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()[:5]
        context['groups'] = Group.objects.all()[:5]
        context['users'] = User.objects.all()[:5]
        context['seachUsers'] = searchUsers
        # context['geodata'] = geodata
        context['login_form'] = AuthenticationForm
        return context

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'