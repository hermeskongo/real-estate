from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.views.generic import ListView, FormView, DetailView

from properties.forms import SearchForm
from properties.models import Properties, Categories


class PropertiesListView(ListView, FormView):
    model = Properties
    form_class = SearchForm
    template_name = "properties.html"
    context_object_name = 'properties'
    
    def get(self, *args, **kwargs):
        response = super(PropertiesListView, self).get(*args, **kwargs)
        
        if self.request.headers.get('HX-Request'):
            return render(self.request, 'includes/results.html', {'properties': self.object_list})
        return response
    
    def get_queryset(self):
        queryset = self.model.objects.filter(is_available=True).order_by('-created_at', '-updated_at')
        
        # Récupération des différents paramètres de filtres
        category = self.request.GET.get('category', None)
        country = self.request.GET.get('country', None)
        min_price = self.request.GET.get('min_price', None)
        max_price = self.request.GET.get('max_price', None)
        
        if (category and country and min_price and max_price) is None:
            pass
        # Application de la recherche si au moins 1 des paramètres est défini
        else:
            if category:
                category_class = get_object_or_404(Categories, id=int(category))
                queryset = queryset.filter(category=category_class)
            if country:
                queryset = queryset.filter(country=country)
            if min_price:
                queryset = queryset.filter(price__gte=min_price)
            if max_price:
                queryset = queryset.filter(price__lte=max_price)
        
        return queryset
    
    def get_context_data(self, *args, **kwargs):
        context = super(PropertiesListView, self).get_context_data(*args, **kwargs)
        
        if self.request.headers.get('HX-Request'):
            context['title'] = 'Résultats de votre recherche'
        else:
            context['title'] = 'Tous nos biens immobiliers'
        return context


class PropertiesDetailView(DetailView):
    model = Properties
    template_name = 'details.html'
    context_object_name = 'property'
    
    def get_object(self, *args, **kwargs):
        pk = int(self.kwargs['id'])
        slug = self.kwargs['slug']
        
        return get_object_or_404(Properties, id=pk, slug=slug)
