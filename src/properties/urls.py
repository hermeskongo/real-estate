from django.urls import path

from properties.views import PropertiesListView, PropertiesDetailView, ContactView

app_name = 'properties'

urlpatterns = [
    path('properties/', PropertiesListView.as_view(),name='index'),
    path('properties/<slug:slug>-<int:id>/', PropertiesDetailView.as_view(), name='details'),
    path('contact/', ContactView.as_view(), name='contact')
]
