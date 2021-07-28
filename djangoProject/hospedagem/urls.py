from django.urls import path
from . import views

urlpatterns = [
    path('', views.hospedagens, name='hospedagens'),
    path('hospedagem/<int:hosp_id>', views.hospedagem, name='hospedagem-page'),
]
