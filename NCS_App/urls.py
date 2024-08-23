from django.urls import path
from . import views

urlpatterns = [
    path('ncs/', views.ncs, name = "ncs"),
    path('ncs_result/', views.ncs_result, name = "ncs_result"),
    path('ncs_back/', views.ncs_back, name = "ncs_back"),
]