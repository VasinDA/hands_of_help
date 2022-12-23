from django.urls import path
from .views import OffersListView, OffersDetailView, OffersCreateView, OffersUpdateView, OffersDeleteView

urlpatterns = [
    path("", OffersListView.as_view(), name="offers_list"),
    path("offers/<int:pk>", OffersDetailView.as_view(), name="offers_detail"),
    path("offers/new", OffersCreateView.as_view(), name="offers_new"),
    path("offers/<int:pk>/edit/", OffersUpdateView.as_view(), name="offers_edit"),
    path("offers/<int:pk>/detele", OffersDeleteView.as_view(), name="offers_delete"),
]