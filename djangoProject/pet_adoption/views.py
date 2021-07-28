from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory
from .models import Pet
from .forms import PetAdoptionForm


@login_required
def adoption_page(request):
    context = {
        'title': 'Adoption Page',
        'pets': Pet.objects.filter(dono=None)
    }
    return render(request, 'pet_adoption/pet_adoption.html', context)


@login_required
def pet(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    if request.method == 'POST':
        partial_adoption_form = modelform_factory(Pet, PetAdoptionForm, ['data_adocao'])
        adoption_form = partial_adoption_form(request.POST, instance=pet)
        if adoption_form.is_valid():
            pet.dono = request.user
            adoption_form.save()
            messages.success(request, f'Você acabou de adotar o Pet {pet}!')
            return redirect('adoption-page')
        else:
            messages.error(request, f'Não foi possível adotar o Pet {pet}. Tente novamente mais tarde.')
            return redirect('pet-page', pet_id=pet_id)
    else:
        context = {
            'pet': pet,
            'adoption_form': PetAdoptionForm,
            'title': 'Adoção',
        }
        return render(request, "pet_adoption/pet_page.html", context)

