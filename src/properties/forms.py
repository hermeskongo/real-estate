from django import forms

from properties.models import Properties, Messages


class SearchForm(forms.ModelForm):
    min_price = forms.IntegerField()
    max_price = forms.IntegerField()
    
    class Meta:
        model = Properties
        fields = ['category', 'country', ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.required = False


class MessagesForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['subject', 'first_name', 'last_name', 'email','phone_number', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
