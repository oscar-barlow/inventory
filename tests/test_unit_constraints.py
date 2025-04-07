import pytest
import uuid
from django.db import IntegrityError, transaction
from inventory.models.unit_of_measure import UnitOfMeasure


@pytest.mark.django_db
class TestUnitOfMeasureConstraints:
    """Test database constraints are properly enforced for UnitOfMeasure."""

    def test_unique_constraints(self):
        """Test unique constraints on UnitOfMeasure."""
        # Create a unit
        UnitOfMeasure.objects.create(name="Test Unit", abbreviation="tu")
        
        # Try to create another unit with the same name - should raise IntegrityError
        with pytest.raises(IntegrityError):
            with transaction.atomic():
                UnitOfMeasure.objects.create(name="Test Unit", abbreviation="tu2")
        
        # Try to create another unit with the same abbreviation - should raise IntegrityError
        with pytest.raises(IntegrityError):
            with transaction.atomic():
                UnitOfMeasure.objects.create(name="Test Unit 2", abbreviation="tu")

    def test_not_null_constraints(self):
        """Test not null constraints on UnitOfMeasure."""
        # Try to create a unit with null name
        with pytest.raises(IntegrityError):
            with transaction.atomic():
                UnitOfMeasure.objects.create(name=None, abbreviation="tu")
        
        # Try to create a unit with null abbreviation
        with pytest.raises(IntegrityError):
            with transaction.atomic():
                UnitOfMeasure.objects.create(name="Test Unit", abbreviation=None)
    
    def test_uuid_primary_keys(self):
        """Test that UUIDs are properly generated as primary keys."""
        # Create a unit
        unit = UnitOfMeasure.objects.create(name="Test Unit", abbreviation="tu")
        
        # Verify UUID was generated
        assert unit.id is not None
        
        # Verify it's in the correct UUID format (length and type)
        assert len(str(unit.id)) == 36  # Standard UUID string length
        assert "-" in str(unit.id)  # UUID format includes hyphens
        
        # Test that ID is a valid UUID
        assert isinstance(unit.id, uuid.UUID)