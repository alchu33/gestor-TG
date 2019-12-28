from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.contrib import messages
from django.urls import reverse_lazy

#importando vistas genéricas
#las vistas genéricas ayudan a ahorrar código
#en caso de que no existan se utilizan funciones
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from ..decorators import admin_permissions
from django.contrib.auth.decorators import login_required

from ..models import ProposalStatus


@method_decorator([login_required, admin_permissions], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'managerApp/proposalstatus/index.html'
    context_object_name = 'proposalstatus_list'
    
    def get_queryset(self):
        return ProposalStatus.objects.order_by('id')[:10]


@method_decorator([login_required, admin_permissions], name='dispatch')
class CreateProposalStatusView(generic.CreateView):
    model = ProposalStatus
    fields = "__all__"
    template_name = 'managerApp/proposalstatus/create.html'

    def form_valid(self, form):
        proposalstatus = form.save(commit=False)
        proposalstatus.save()
        messages.success(self.request, 'Fue creao un nuevo tipo de estatus de propuesta')
        return redirect('proposal_status:proposal_status_list')


@method_decorator([login_required, admin_permissions], name='dispatch')
class UpdateProposalStatusView(generic.UpdateView):
    model = ProposalStatus
    fields = "__all__"
    template_name = 'managerApp/proposalstatus/update.html'

    def form_valid(self, form):
        proposalstatus = form.save(commit=False)
        proposalstatus.save()
        messages.success(self.request, 'Fue modificado un tipo de estatus de propuesta')
        return redirect('proposal_status:proposal_status_list')


@method_decorator([login_required, admin_permissions], name='dispatch')
class DeleteProposalStatusView(generic.DeleteView):
    model = ProposalStatus
    template_name = 'managerApp/proposalstatus/delete.html'
    success_url = reverse_lazy('proposal_status:proposal_status_list')
