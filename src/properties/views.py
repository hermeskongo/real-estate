from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, FormView

from properties.forms import SearchForm
from properties.models import Properties


class PropertiesListView(ListView, FormView):
    model = Properties
    form_class = SearchForm
    template_name = "properties.html"
    context_object_name = 'properties'
    
    def get_queryset(self):
        return self.model.objects.filter(is_available=True).order_by('-created_at', '-updated_at')
    