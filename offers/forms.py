from django import forms
from offers.models import Offers

class CreationOffersForm(forms.ModelForm):
    title = forms.CharField(label='Вкажіть назву', min_length=10)
    body = forms.Textarea()
    url_image = forms.URLField(label='Посилання на фото')
    location= forms.CharField(label='Місцезнаходження')
    
    class Meta:
        model = Offers
        fields = ['title', 'body', 'url_image', 'location']
    