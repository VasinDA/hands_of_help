from django import forms
from requests.models import Requests

class CreationRequestsForm(forms.ModelForm):
    title = forms.CharField(label='Назва', min_length=10)
    body = forms.Textarea()
    location= forms.CharField(label='Місцезнаходження')
    
    class Meta:
        model = Requests
        fields = ['title', 'body', 'location']
        
class UpdateRequestsForm(forms.ModelForm):
    title = forms.CharField(label='Назва', min_length=10)
    body = forms.Textarea()

    class Meta:
        model = Requests
        fields = ['title', 'body']
