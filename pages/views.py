from .forms import ContactForm
from offers.models import Offers
from django.views.generic import ListView
from django.views.generic import TemplateView

class HomePageView(ListView):
    model = Offers    
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offers_list'] = Offers.objects.all().order_by('-date')[:5]
        return context

class AboutPageView(TemplateView):
    template_name = "about.html"

class ContactsPageView(TemplateView):
    template_name = "contacts.html"