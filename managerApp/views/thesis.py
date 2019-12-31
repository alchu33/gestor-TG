from . import *


# para no repetir
THESIS_CRUD_FIELDS = (
    "title",
    "status",
    "nrc",
    "descriptors",
    "thematic_category",
    "top_date",
    "company_name",
    "term",
    "proposal"
)

@method_decorator([login_required, guest_permissions], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'managerApp/thesis/index.html'
    context_object_name = 'thesis_list'
    
    def get_queryset(self):
        return Thesis.objects.order_by('id')

@method_decorator([login_required, guest_permissions], name='dispatch')
class DetailView(generic.DetailView):
    model = Thesis
    template_name = 'managerApp/thesis/detail.html'

@method_decorator([login_required, manager_permissions], name='dispatch')
class CreateThesisView(generic.CreateView):
    model = Thesis
    fields = THESIS_CRUD_FIELDS
    template_name = 'managerApp/thesis/create.html'

    def form_valid(self, form):
        thesis = form.save(commit=False)
        thesis.save()
        messages.success(self.request, 'La thesis fue creada satisfactoriamente')
        return redirect('thesis:thesis_list')

@method_decorator([login_required, manager_permissions], name='dispatch')
class UpdateThesisView(generic.UpdateView):
    model = Thesis
    fields = THESIS_CRUD_FIELDS
    template_name = 'managerApp/thesis/update.html'

    def form_valid(self, form):
        thesis = form.save(commit=False)
        thesis.save()
        messages.success(self.request, 'La propuesta fue actualizada satisfactoriamente')
        return redirect('thesis:thesis_list')

@method_decorator([login_required, manager_permissions], name='dispatch')
class DeleteThesisView(generic.DeleteView):
    model = Thesis
    template_name = 'managerApp/thesis/delete.html'
    success_url = reverse_lazy('thesis:thesis_list')