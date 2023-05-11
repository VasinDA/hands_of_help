from offers.forms import CreationOffersForm
from .forms import CreationRequestsForm, UpdateRequestsForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy, reverse
from offers.models import Offers
from .models import Requests
from django.db.models import Q

class OfferGet(DetailView):
    model = Requests
    template_name = "requests_detail.html"

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        request = self.object
        request_in_offer =  request.offer.all()
        context["request_in_offer"] =  request_in_offer
        if request_in_offer:
            context["offer_id"] = request.offer.values("id").first()["id"]
            return context
        if self.request.user.is_superuser:
           context["form"] = CreationRequestsForm() 
           context["offers_list"] = request.offers_set.all().order_by('-date')
           return context
        if self.request.user.is_authenticated:
           context["form"] = CreationRequestsForm() 
           context["offers_list"] = request.offers_set.filter(Q(author_id=self.request.user) | Q(status_id=2)).order_by('-date')
           return context
        context["offers_list"] = request.offers_set.filter(status_id=2).order_by('-date')
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
        offer.save()
        request = self.object
        offer.request.add(request)
        return super().form_valid(form)
    
    def get_success_url(self):
        request = self.get_object() 
        return reverse("requests_detail", kwargs={"pk": request.pk})

class RequestsListView(ListView):
    model = Requests
    template_name = "requests_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_superuser:
            context['requests_list'] = Requests.objects.exclude(offer__isnull=False).order_by('-date')
        if self.request.user.is_authenticated:
            context['requests_list'] = Requests.objects.exclude(offer__isnull=False).filter(Q(author_id=self.request.user) | Q(status_id=2)).order_by('-date')
        context['requests_list'] = Requests.objects.exclude(offer__isnull=False).filter(status_id=2).order_by('-date')
        return context

class RequestsDetailView(DetailView):
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

    def form_valid(self, form):
        request = self.object
        offers = request.offers_set.all()
        offers.delete()
        return super().form_valid(form)
 
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user or self.request.user.is_superuser