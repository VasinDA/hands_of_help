from .forms import CreationOffersForm, UpdateOffersForm
from requests.forms import CreationRequestsForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy, reverse
from requests.models import Requests
from .models import Offers

class RequestGet(DetailView):
    model = Offers
    template_name = "offers_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CreationRequestsForm()
        context["requests_list"] = Requests.objects.filter(offer_id=self.get_object().pk).order_by('-date')
        return context
    
class RequestPost(SingleObjectMixin, FormView):
    model = Offers
    form_class = CreationRequestsForm
    template_name = "offers_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        request = form.save(commit=False)
        request.author = self.request.user
        request.request = self.object
        request.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        offer = self.get_object()
        return reverse("offers_detail", kwargs={"pk": offer.pk})

class OffersListView(ListView):
    model = Offers
    template_name = "offers_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offers_list'] = Offers.objects.filter(request_id__isnull=True).order_by('-date')
        return context

class OffersDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        view = RequestGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = RequestPost.as_view()
        return view(request, *args, **kwargs)

class OffersCreateView(LoginRequiredMixin, CreateView):
    form_class = CreationOffersForm
    template_name = "offers_new.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class OffersUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Offers
    form_class = UpdateOffersForm
    template_name = "offers_edit.html"
    
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