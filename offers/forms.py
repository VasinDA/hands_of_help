from django import forms
from offers.models import Offers

class CreationOffersForm(forms.ModelForm):
    title = forms.CharField(label='Назва', min_length=10)
    body = forms.Textarea()
    url_image = forms.URLField(label='Посилання на фото')
    location= forms.CharField(label='Місцезнаходження')
    status = forms.ChoiceField(label='Статус')
    
    class Meta:
        model = Offers
        fields = ['title', 'body', 'url_image', 'location', 'status']
        
class UpdateOffersForm(forms.ModelForm):
    title = forms.CharField(label='Назва', min_length=10)
    body = forms.Textarea()
    status = forms.ChoiceField(label='Статус')

    class Meta:
        model = Offers
        fields = ['title', 'body','url_image', 'status']