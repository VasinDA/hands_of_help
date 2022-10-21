from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class ContactsPageView(TemplateView):
    template_name = "contacts.html"