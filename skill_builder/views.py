from django.http import request

from django.shortcuts import render
from django.views import generic
from .models import Skill, SubSkill



# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'home.html'


class SkillView(generic.ListView):
    template_name = 'skills.html'
    model = Skill


class SubSkillView(generic.ListView):
    queryset = SubSkill.objects.all()
    template_name = "skill.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SubSkillView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


def sub_skill_list_view(request, pk=None, *args, **kwargs):
    object = SubSkill.objects.get(skill=pk)
    context = {
        'object_list': object
    }
    return  render(request, "skill.html", context)


class HomePageView(generic.ListView):
    template_name = 'skill.html'
    model = SubSkill
    context_object_name = 'object_list'

    def get_queryset(self):
        contacts = super().get_queryset()
        return contacts.filter(skill=self.kwargs['pk'])

class AddSkillsView(generic.CreateView):
    template_name = 'new_skill.html'
    model = Skill
    fields = ['title', 'progress','learning_time']

    def get_initial(self, ):
        initial = super().get_initial()
        return initial


class AddSubSkillsView(generic.CreateView):
    template_name = 'new_sub_skill.html'
    model = SubSkill
    fields = ['title', 'progress', 'learning_time', 'skill', 'text']

    def get_initial(self, ):
        initial = super().get_initial()
        return initial


