from django.views.generic import (ListView, DetailView, UpdateView, DeleteView,
                                    TemplateView, CreateView)

from posts.models import Post
from groups.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()

class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()[:5]
        context['groups'] = Group.objects.all()[:5]
        context['users'] = User.objects.all()[:5]
        return context

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'