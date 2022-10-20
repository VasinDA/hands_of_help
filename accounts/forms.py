from django import forms
from django.contrib.auth.models import User
from bootstrap_modal_forms.forms import BSModalModelForm
 
class UserRegisterForm(BSModalModelForm):
  email = forms.EmailField()
 
  class Meta:
      model = User
      fields = ['username', 'first_name', 'last_name', 'email']