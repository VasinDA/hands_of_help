from django.views import View
from .forms import CreationOffersForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy, reverse
from .models import Offers

class OffersListView(ListView):
    model = Offers
    template_name = "offers_list.html"

class OffersDetailView(LoginRequiredMixin, DetailView):
    model = Offers
    template_name = "offers_detail.html"

class OffersCreateView(LoginRequiredMixin, CreateView):
    model = CreationOffersForm
    template_name = "offers_new.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class OffersUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Offers
    template_name = "offers_edit.html"
    fields = ["title", "body"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class OffersDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Offers
    template_name = "offers_delete.html"
    success_url = reverse_lazy("offers_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user