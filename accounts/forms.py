from django import forms
from accounts.models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
 
class UserRegisterForm(UserCreationForm):
  username = forms.CharField(label='Користувач', min_length=3, max_length=150)
  first_name = forms.CharField(label="Ім'я", max_length=150)
  last_name = forms.CharField(label='Призвище', max_length=150)
  email = forms.EmailField(label='Пошта')
  phone = forms.CharField(label='Телефон', min_length=10, max_length=15)
  password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)  
  password2 = forms.CharField(label='Підтвердити пароль', widget=forms.PasswordInput)

  class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 
        'password1', 'password2')

  def username_clean(self):  
    username = self.cleaned_data['username'].lower()  
    new = CustomUser.objects.filter(username = username)  
    if new.count():  
      raise ValidationError("Такий користувач вже існує")  
    return username
    
  def email_clean(self):  
    email = self.cleaned_data['email'].lower()  
    new = CustomUser.objects.filter(email = email)
    if new.count():  
        raise ValidationError("Такий Email вже існує в базі")  
    return email  
  
  def clean_password(self):  
    password1 = self.cleaned_data['password1']  
    password2 = self.cleaned_data['password2']  
    if password1 and password2 and password1 != password2:  
      raise ValidationError("Паролі не співпадають")  
    return password2  
  
  def save(self, commit = True):  
    user = CustomUser.objects.create_user(  
      self.cleaned_data['username'],
      self.cleaned_data['email'],  
      self.cleaned_data['password1'],
      first_name = self.cleaned_data['first_name'],
      last_name = self.cleaned_data['last_name'],
      phone = self.cleaned_data['phone'],
      )  
    return user

class UserChangePassword(UserChangeForm):
  password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)  
  password2 = forms.CharField(label='Підтвердити пароль', widget=forms.PasswordInput)

  class Meta:  
    model = CustomUser
    fields = ('password1', 'password2')
  
  def clean_password(self):  
    password1 = self.cleaned_data['password1']  
    password2 = self.cleaned_data['password2']  
    if password1 and password2 and password1 != password2:  
      raise ValidationError("Паролі не співпадають")  
    return password2