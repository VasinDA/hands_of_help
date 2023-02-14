from django.urls import path
from .views import RequestsListView, RequestsDetailView, RequestsCreateView, RequestsUpdateView, RequestsDeleteView

urlpatterns = [
    path("", RequestsListView.as_view(), name="requests_list"),
    path("requests/<int:pk>", RequestsDetailView.as_view(), name="requests_detail"),
    path("requests/new", RequestsCreateView.as_view(), name="requests_new"),
    path("requests/<int:pk>/edit/", RequestsUpdateView.as_view(), name="requests_edit"),
    path("requests/<int:pk>/detele/", RequestsDeleteView.as_view(), name="requests_delete"),
]