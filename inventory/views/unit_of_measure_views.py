from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from inventory.models import UnitOfMeasure
from inventory.forms import UnitOfMeasureForm


class UnitOfMeasureListView(ListView):
    model = UnitOfMeasure
    template_name = 'inventory/unit_list.html'
    context_object_name = 'units'


class UnitOfMeasureCreateView(CreateView):
    model = UnitOfMeasure
    template_name = 'inventory/unit_form.html'
    form_class = UnitOfMeasureForm
    success_url = reverse_lazy('inventory:unit-list')
