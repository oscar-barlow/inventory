from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from inventory.models import InventoryItem
from inventory.forms import InventoryItemForm


class InventoryItemListView(ListView):
    model = InventoryItem
    template_name = 'inventory/inventory_list.html'
    context_object_name = 'items'


class InventoryItemDetailView(DetailView):
    model = InventoryItem
    template_name = 'inventory/inventory_detail.html'
    context_object_name = 'item'


class InventoryItemCreateView(CreateView):
    model = InventoryItem
    template_name = 'inventory/inventory_form.html'
    form_class = InventoryItemForm
    success_url = reverse_lazy('inventory:item-list')


class InventoryItemUpdateView(UpdateView):
    model = InventoryItem
    template_name = 'inventory/inventory_form.html'
    form_class = InventoryItemForm
    success_url = reverse_lazy('inventory:item-list')


class InventoryItemDeleteView(DeleteView):
    model = InventoryItem
    template_name = 'inventory/inventory_confirm_delete.html'
    success_url = reverse_lazy('inventory:item-list')
