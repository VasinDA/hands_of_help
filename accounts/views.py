from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import UserRegisterForm, UserChangePassword
 
class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
    success_message = "Ваш профіль успішно створено"

class ChangePasswordView(UpdateView):
    form_class = UserChangePassword
    success_url = reverse_lazy('login')
    template_name = "registration/changepassword.html"
    success_message = "Ваш пароль успішно змінено"

    def get_object(self, queryset=None):
        return self.request.user

    def get_form_kwargs(self):
        kwargs = super(ChangePasswordView, self).get_form_kwargs()
        kwargs['user'] = kwargs.pop('instance')
        return kwargs