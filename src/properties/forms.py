from django import forms

from properties.models import Properties


class SearchForm(forms.ModelForm):
    min_price = forms.IntegerField()
    max_price = forms.IntegerField()
    
    class Meta:
        model = Properties
        fields = ['name', 'category', 'bedrooms', 'bathrooms', 'rooms', 'country', 'surface']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            