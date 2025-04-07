import uuid
from django.db import models
from inventory.models.unit_of_measure import UnitOfMeasure


class InventoryItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    unit = models.ForeignKey(UnitOfMeasure, on_delete=models.CASCADE, related_name='items')
    quantity = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit.abbreviation})"
        
    class Meta:
        # Add options for STRICT table mode with SQLite
        constraints = [
            models.CheckConstraint(condition=models.Q(id__isnull=False), name='inventory_id_not_null')
        ]
