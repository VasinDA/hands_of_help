from django import forms
from urllib import request
from django.contrib.auth.hashers import check_password
from accounts.models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
 
class UserRegisterForm(UserCreationForm):
  username = forms.CharField(label='Користувач', min_length=3, max_length=150)
  first_name = forms.CharField(label="Ім'я", max_length=150, required=False)
  last_name = forms.CharField(label='Призвище', max_length=150, required=False)
  email = forms.EmailField(label='Пошта')
  phone = forms.CharField(label='Телефон', min_length=10, max_length=15)
  password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)  
  password2 = forms.CharField(label='Підтвердити пароль', widget=forms.PasswordInput)

  class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 
        'password1', 'password2')

  def clean_username(self):  
    username = self.cleaned_data['username'].lower()  
    new = CustomUser.objects.filter(username = username)  
    if new.count():  
      raise ValidationError("Такий користувач вже існує")  
    return username
    
  def clean_email(self):  
    email = self.cleaned_data['email'].lower()  
    new = CustomUser.objects.filter(email = email)
    if new.count():  
        raise ValidationError("Такий Email вже існує в базі")  
    return email  
  
  def clean_password2(self):
    password1 = self.cleaned_data['password1']  
    password2 = self.cleaned_data['password2']  
    if (password1 !="" and password2 !="") and (password1 != password2):  
        raise ValidationError("Паролі не співпадають")
    return password2

class UserChangePassword(PasswordChangeForm):
  old_password = forms.CharField(label='Старий пароль', widget=forms.PasswordInput)
  new_password1 = forms.CharField(label='Новий пароль', widget=forms.PasswordInput)  
  new_password2 = forms.CharField(label='Підтвердити новий пароль', widget=forms.PasswordInput)
  
  class Meta:  
    model = CustomUser
    fields = ('old_password', 'new_password1', 'new_password2')
  
  def clean_old_password(self):  
    try:
      return super(UserChangePassword, self).clean_old_password()
    except forms.ValidationError:
      raise forms.ValidationError("Ввели не вірний пароль")
    
        
  def clean_new_password2(self):
    new_password1 = self.cleaned_data['new_password1']
    new_password2 = self.cleaned_data['new_password2']
    if (new_password1 != "" and new_password2 != "") and (new_password1 != new_password2):
          raise ValidationError("Паролі не співпадають")  
    return new_password2