from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(request, f'Usuário criado para {username}')
            return redirect('adoption-page')
    else:
        register_form = UserRegisterForm()
    context = {
        'register_form': register_form,
        'title': 'Cadastro'
    }
    return render(request, 'home/register.html', context)


@login_required
def home_page(request):
    context = {
        'title': 'Home Page',
    }
    return render(request, 'home/home.html', context)
