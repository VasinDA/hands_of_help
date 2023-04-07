from django import forms
from offers.models import Offers
from statuses.models import Status

class CreationOffersForm(forms.ModelForm):
    title = forms.CharField(label='Назва', min_length=10)
    body = forms.Textarea()
    url_image = forms.URLField(label='Посилання на фото')
    location= forms.CharField(label='Місцезнаходження')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Статус', initial=2)
    
    class Meta:
        model = Offers
        fields = ['title', 'body', 'url_image', 'location', 'status']
        
class UpdateOffersForm(forms.ModelForm):
    title = forms.CharField(label='Назва', min_length=10)
    body = forms.Textarea()
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Статус', empty_label='Виберіть статус')

    class Meta:
        model = Offers
        fields = ['title', 'body','url_image', 'status']