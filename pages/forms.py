from django import forms
 
class ContactForm(forms.Form):
  email = forms.EmailField()
  message = forms.CharField()
 
  class Meta:
      fields = ['first_name', 'last_name', 'email', 'message']