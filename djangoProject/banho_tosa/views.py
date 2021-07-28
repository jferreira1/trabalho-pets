from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory
from .models import Estabelecimento, ReservaEstabelecimento
from .forms import ReservaHospedagemForm


@login_required
def estabelecimentos(request):
    context = {
        'title': 'Estabelecimentos',
        'estabs': Estabelecimento.objects.all()
    }
    return render(request, 'banho_tosa/estabelecimentos.html', context)


@login_required
def estabelecimento(request, estab_id):
    estab = Estabelecimento.objects.get(id=estab_id)
    reserva = ReservaEstabelecimento(user=request.user, estabelecimento=estab, valor_total=estab.valor)
    if request.method == 'POST':
        partial_reserva_form = modelform_factory(ReservaEstabelecimento, ReservaHospedagemForm, ['agendamento'])
        reserva_form = partial_reserva_form(request.POST, instance=reserva)
        if reserva_form.is_valid():
            reserva_form.save()
            messages.success(request, f'Você acabou de agendar um serviço de banho e tosa no estabelecimento {estab}!')
            return redirect('estabelecimentos')
        else:
            messages.error(request, f'Não foi possível agendar para o estabelecimento {estab}. Tente novamente mais tarde.')
            return redirect('estabelecimento-page', estad_id=estab.id)
    else:
        context = {
            'estab': estab,
            'estab_form': ReservaHospedagemForm,
            'title': 'Banho e Tosa',
        }
        return render(request, "banho_tosa/estabelecimento.html", context)

