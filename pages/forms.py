from django import forms
 
class ContactForm(forms.Form):
  first_name = forms.CharField(label="Ім'я", min_length=5)
  email = forms.EmailField(label="Пошта")
  message = forms.CharField(label="Повідомлення", widget=forms.Textarea)
 
  class Meta:
      fields = ['first_name', 'email', 'message']