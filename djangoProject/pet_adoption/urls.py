from django.urls import path
from . import views

urlpatterns = [
    path('', views.adoption_page, name='adoption-page'),
    path('pet/<int:pet_id>', views.pet, name='pet-page'),
]
