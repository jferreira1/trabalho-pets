from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory
from .models import Hospedagem, ReservaHospedagem
from .forms import ReservaHospedagemForm


@login_required
def hospedagens(request):
    context = {
        'title': 'Hospedagem',
        'hosps': Hospedagem.objects.all()
    }
    return render(request, 'hospedagem/hospedagens.html', context)


@login_required
def hospedagem(request, hosp_id):
    hosp = Hospedagem.objects.get(id=hosp_id)
    reserva = ReservaHospedagem(user=request.user, hospedagem=hosp, valor_total=hosp.valor_diaria)
    if request.method == 'POST':
        partial_reserva_form = modelform_factory(ReservaHospedagem, ReservaHospedagemForm, ['data_reserva'])
        reserva_form = partial_reserva_form(request.POST, instance=reserva)
        if reserva_form.is_valid():
            reserva_form.save()
            messages.success(request, f'Você acabou de reservar a Hospedagem {hosp}!')
            return redirect('hospedagens')
        else:
            messages.error(request, f'Não foi possível reservar a Hospedagem {hosp}. Tente novamente mais tarde.')
            return redirect('hospedagem-page', hosp_id=hosp.id)
    else:
        context = {
            'hosp': hosp,
            'hosp_form': ReservaHospedagemForm,
            'title': 'Hospedagem',
        }
        return render(request, "hospedagem/hospedagem.html", context)

