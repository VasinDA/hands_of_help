from django import forms
from requests.models import Requests

class CreationRequestsForm(forms.ModelForm):
    title = forms.CharField(label='Назва', min_length=10)
    body = forms.Textarea()
    location= forms.CharField(label='Місцезнаходження')
    status = forms.ChoiceField(label='Статус')
    
    class Meta:
        model = Requests
        fields = ['title', 'body', 'location', 'status']
        
class UpdateRequestsForm(forms.ModelForm):
    title = forms.CharField(label='Назва', min_length=10)
    body = forms.Textarea()
    status = forms.ChoiceField(label='Статус')

    class Meta:
        model = Requests
        fields = ['title', 'body', 'status']
