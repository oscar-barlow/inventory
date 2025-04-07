import uuid
from django.db import models


class UnitOfMeasure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return self.name
        
    class Meta:
        # Add options for STRICT table mode with SQLite
        constraints = [
            models.CheckConstraint(condition=models.Q(id__isnull=False), name='unit_id_not_null')
        ]
