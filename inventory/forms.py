from django import forms
from inventory.models import InventoryItem, UnitOfMeasure


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, (forms.CharField, forms.FloatField, forms.IntegerField)):
                field.widget.attrs.update({'class': 'form-control'})
            elif isinstance(field, forms.ModelChoiceField):
                field.widget.attrs.update({'class': 'form-select'})


class InventoryItemForm(BootstrapModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'description', 'unit', 'quantity']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class UnitOfMeasureForm(BootstrapModelForm):
    class Meta:
        model = UnitOfMeasure
        fields = ['name', 'abbreviation']