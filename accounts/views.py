from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
from .forms import UserRegisterForm

 
class SignUpView(BSModalCreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('')
    template_name = "registration/signup.html"
    success_message = "Ваш профіль успішно створено"