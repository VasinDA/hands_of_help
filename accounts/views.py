from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegisterForm, UserChangePassword

 
class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
    success_message = "Ваш профіль успішно створено"

class ChangePasswordView(CreateView):
    form_class = UserChangePassword
    success_url = reverse_lazy('login')
    template_name = "registration/changepassword.html"
    success_message = "Ваш пароль успішно змінено"