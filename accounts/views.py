from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegisterForm
 
class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
    success_message = "Your profile was created successfully"