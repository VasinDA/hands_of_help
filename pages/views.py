from .forms import ContactForm
from offers.models import Offers
from requests.models import Requests
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.generic.edit import FormView
from django.views.generic.detail import SingleObjectMixin

class HomePageView(ListView):
    model = Offers # why work without Requests model
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offers_list'] = Offers.objects.exclude(request__isnull=False).filter(status_id=2).order_by('-date')[:5]
        context['requests_list'] = Requests.objects.exclude(offer__isnull=False).filter(status_id=2).order_by('-date')[:5]
        return context

class AboutPageView(TemplateView):
    template_name = "about.html"

class ContactsPageView(FormView):
    form_class = ContactForm
    template_name = "contacts.html"
    success_url = reverse_lazy("contacts")

    def form_valid(self, form):
        subject = 'Новое сообщение от {}'.format(form.cleaned_data['first_name'])
        message = 'От: {}\n\n{}'.format(
            form.cleaned_data['email'],
            form.cleaned_data['message'])
        from_email = 'handsofhelpukraine@gmail.com'
        recipient_list = ['handsofhelpukraine@gmail.com']
        send_mail(subject, message, from_email, recipient_list)
        return super().form_valid(form)