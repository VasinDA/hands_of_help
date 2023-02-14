from django import forms
from offers.models import Offers

class CreationOffersForm(forms.ModelForm):
    title = forms.CharField(label='Назва', min_length=10)
    body = forms.Textarea()
    url_image = forms.URLField(label='Посилання на фото')
    location= forms.CharField(label='Місцезнаходження')
    
    class Meta:
        model = Offers
        fields = ['title', 'body', 'url_image', 'location']
        
class UpdateOffersForm(forms.ModelForm):
    title = forms.CharField(label='Назва', min_length=10)
    body = forms.Textarea()

    class Meta:
        model = Offers
        fields = ['title', 'body']