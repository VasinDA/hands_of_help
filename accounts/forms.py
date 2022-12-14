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
  
  def clean(self):
    cleaned_data = super().clean()  
    password1 = cleaned_data.get('password1')  
    password2 = cleaned_data.get('password2')  
    if password1 and password2 and password1 != password2:  
        raise ValidationError("Паролі не співпадають")  
  
  

class UserChangePassword(PasswordChangeForm):
  old_password = forms.CharField(label='Старий пароль', widget=forms.PasswordInput)
  new_password1 = forms.CharField(label='Новий пароль', widget=forms.PasswordInput)  
  new_password2 = forms.CharField(label='Підтвердити новий пароль', widget=forms.PasswordInput)
  
  class Meta:  
    model = CustomUser
    fields = ('old_password', 'new_password1', 'new_password2')
  
  def clean_password(self):  
    user = CustomUser.objects.get(username=request.user)
    old_password = self.cleaned_data['old_password']
    new_password1 = self.cleaned_data['new_password1']
    new_password2 = self.cleaned_data['new_password2']
    if not check_password(old_password, user.password):
      raise ValidationError("Ввели не вірний пароль")
    if new_password1 and new_password2 and new_password1 != new_password2:  
      raise ValidationError("Паролі не співпадають")  
    return new_password2