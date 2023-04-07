from django import forms
from requests.models import Requests
from statuses.models import Status

class CreationRequestsForm(forms.ModelForm):
    title = forms.CharField(label='Назва', min_length=10)
    body = forms.Textarea()
    location= forms.CharField(label='Місцезнаходження')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Статус', initial=2)
    
    class Meta:
        model = Requests
        fields = ['title', 'body', 'location', 'status']
        
class UpdateRequestsForm(forms.ModelForm):
    title = forms.CharField(label='Назва', min_length=10)
    body = forms.Textarea()
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Статус', empty_label='Виберіть статус')

    class Meta:
        model = Requests
        fields = ['title', 'body', 'status']