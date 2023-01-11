from .forms import ContactForm
from offers.models import Offers
from django.views.generic import ListView
from django.views.generic import TemplateView

class HomePageView(ListView):
    model = Offers    
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offers'] = Offers.objects.all()
        return context

class AboutPageView(TemplateView):
    template_name = "about.html"

class ContactsPageView(TemplateView):
    template_name = "contacts.html"