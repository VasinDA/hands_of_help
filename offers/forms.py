from django import forms
from offers.models import Offers

class CreationOffersForm(forms.ModelForm):
    title = forms.CharField(label='Вкажіть назву', min_length=10)
    body = forms.CharField(label='Опис', min_length=50)
    url_image = forms.URLField(label='Посилання на фото')
    location= forms.TimeField(label='Місцезнаходження')
    

    class Meta:
        model = Offers
        fields = '__all__'
    