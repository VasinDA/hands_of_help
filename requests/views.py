from django.views import View
from .forms import CreationRequestsForm, UpdateRequestsForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy, reverse
from .models import Requests

class RequestsListView(ListView):
    model = Requests
    template_name = "requests_list.html"

class RequestsDetailView(LoginRequiredMixin, DetailView):
    model = Requests
    template_name = "requests_detail.html"

class RequestsCreateView(LoginRequiredMixin, CreateView):
    form_class = CreationRequestsForm
    template_name = "requests_new.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RequestsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Requests
    form_class = UpdateRequestsForm
    template_name = "requests_edit.html"
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class RequestsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Requests
    template_name = "requests_delete.html"
    success_url = reverse_lazy("requests_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user