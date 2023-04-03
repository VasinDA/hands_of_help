from django.views import View
from .forms import CreationRequestsForm, UpdateRequestsForm, CreationOffersForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy, reverse
from .models import Requests

class OfferGet(DeleteView):
    model = Requests
    template_name = "requests_detail.html"

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["form"] = CreationOffersForm()
        return context

class OfferPost(SingleObjectMixin, FormView):
    model = Requests
    form_class = CreationOffersForm
    template_name = "requests_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        offer = form.save(commit=False)
        offer.author = self.request.user
        offer.request = self.object
        offer.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        offer = self.get_object() 
        return reverse("requests_detail", kwargs={"pk": offer.pk})

class RequestsListView(ListView):
    model = Requests
    template_name = "requests_list.html"

class RequestsDetailView(LoginRequiredMixin, DetailView):
    def get(self, request, *args, **kwargs):
        view = OfferGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = OfferPost.as_view()
        return view(request, *args, **kwargs)

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