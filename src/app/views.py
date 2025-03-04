from django.shortcuts import render
from django.views.generic import FormView, ListView

from properties.forms import SearchForm
from properties.models import Properties


class HomeView(ListView, FormView):
    model = Properties
    form_class = SearchForm
    context_object_name = 'properties'
    template_name = 'index.html'
    
    def get_queryset(self):
        return Properties.objects.filter(is_available=True,).order_by('-created_at', '-updated_at')[0:6]
