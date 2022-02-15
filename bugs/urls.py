from django.urls import path, re_path
from django.views.generic.base import RedirectView
from . import views


# app_name = 'tickets'
urlpatterns = [
    path('', views.RedirectHome.as_view(), name='Home'),
    path('tickets', views.TicketListView.as_view(), name='ticket_list'),
    path('tickets/<int:pk>', views.TicketDetailView.as_view(), name='ticket_detail'),
    path('tickets/create', views.TicketCreateView.as_view(), name='ticket_create'),
    path('tickets/delete/<int:pk>', views.TicketDeleteView.as_view(), name='ticket_delete'),
    path('tickets/update/<int:pk>', views.TicketUpdateView.as_view(), name='ticket_update'),
]
