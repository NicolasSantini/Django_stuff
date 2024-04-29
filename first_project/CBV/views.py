from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from . import models

# Create your views here.

class IndexView(TemplateView):
    template_name = 'CBV/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Basic Injection!'
        return context


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School #provides a list of every record in that model

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail' #provide the object itself with all its attributes and stuff
    model = models.School
    template_name = 'CBV/school_detail.html'