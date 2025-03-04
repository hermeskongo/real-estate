from django.urls import path

from properties.views import PropertiesListView

app_name = 'properties'

urlpatterns = [
    path('properties/', PropertiesListView.as_view(),name='index'),
]
