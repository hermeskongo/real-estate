import time

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, CreateView

from properties.forms import SearchForm, MessagesForm
from properties.models import Properties, Categories, Messages


class PropertiesListView(ListView, FormView):
    model = Properties
    form_class = SearchForm
    template_name = "properties.html"
    context_object_name = 'properties'
    paginate_by = 6
    
    def get(self, *args, **kwargs):
        response = super(PropertiesListView, self).get(*args, **kwargs)
        
        if self.request.headers.get('HX-Request'):
            time.sleep(1.5)
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
    
    def get_context_data(self, *args, **kwargs):
        context = super(PropertiesDetailView, self).get_context_data(*args, **kwargs)
        context['form'] = MessagesForm()
        
        return context
    
    def post(self, *args, **kwargs):
        self.object = self.get_object()
        contact_form = MessagesForm(self.request.POST)
        
        if contact_form.is_valid():
            # Récupération des donnés du formulaires pour ensuite récupérer le message envoyé et lui attribué une propriété
            last_name = self.request.POST.get('last_name')
            first_name = self.request.POST.get('first_name')
            email = self.request.POST.get('email')
            phone = self.request.POST.get('phone_number')
            content = self.request.POST.get('content')
            
            
            contact_form.save()
            
            # Récupération du message venant d'être envyé et assignation de la propriété correspondante
            message = Messages.objects.filter(last_name=last_name, first_name=first_name, email=email, phone_number=phone, content=content).last()
            message.properties = self.get_object()
            message.save()
            
            # Messages de succès !
            messages.success(self.request, "Votre message a bien été envoyé. Merci à vous !")
            
            
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = contact_form
            return self.render_to_response(context)
        
        new_path = str(self.request.path) + "#contact-form"
        return redirect(new_path)
    

class ContactView(CreateView):
    model = Messages
    form_class = MessagesForm
    template_name = 'contact.html'
    success_url = reverse_lazy("properties:contact")
    
    def form_valid(self, form):
        messages.success(self.request, "Votre message a bien été envoyé, nous vous reviendrons")
        return super(ContactView, self).form_valid(form)
