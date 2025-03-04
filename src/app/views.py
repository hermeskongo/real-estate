from django.shortcuts import render
from properties.models import Properties
 
def home(request):
    properties = Properties.objects.filter(is_available=True,)[0:6]
    context = {
        'properties': properties,
    }
    return render(request, 'index.html', context=context)
