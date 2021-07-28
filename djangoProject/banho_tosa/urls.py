from django.urls import path
from . import views

urlpatterns = [
    path('', views.estabelecimentos, name='estabelecimentos'),
    path('estabelecimento/<int:estab_id>', views.estabelecimento, name='estabelecimento-page'),
]
