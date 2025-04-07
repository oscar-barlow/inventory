import pytest
import uuid
from django.db import IntegrityError, transaction
from django.db.models import ProtectedError
from inventory.models.unit_of_measure import UnitOfMeasure
from inventory.models.inventory_item import InventoryItem


@pytest.mark.django_db
class TestInventoryItemConstraints:
    """Test database constraints are properly enforced for InventoryItem."""

    def test_not_null_constraints(self):
        """Test not null constraints on InventoryItem."""
        # Create a unit for foreign key reference
        unit = UnitOfMeasure.objects.create(name="Test Unit", abbreviation="tu")
        
        # Try to create an item with null name
        with pytest.raises(IntegrityError):
            with transaction.atomic():
                InventoryItem.objects.create(name=None, unit=unit, quantity=10)
        
        # Try to create an item with null quantity
        with pytest.raises(IntegrityError):
            with transaction.atomic():
                InventoryItem.objects.create(name="Test Item", unit=unit, quantity=None)
        
        # Try to create an item with null unit
        with pytest.raises(IntegrityError):
            with transaction.atomic():
                InventoryItem.objects.create(name="Test Item", unit=None, quantity=10)

    def test_foreign_key_cascade(self):
        """Test foreign key cascade on InventoryItem."""
        # Create a unit and an item
        unit = UnitOfMeasure.objects.create(name="Test Unit", abbreviation="tu")
        item = InventoryItem.objects.create(name="Test Item", unit=unit, quantity=10)
        
        # Store the item id for later verification
        item_id = item.id
        
        # Since we're using CASCADE, we need to verify that the item gets deleted when unit is deleted
        unit.delete()
        
        # Verify the item was deleted due to cascade
        assert InventoryItem.objects.filter(id=item_id).count() == 0
        
    @pytest.mark.django_db(transaction=True)
    def test_foreign_key_constraint(self):
        """Test that foreign key constraints prevent invalid references."""
        with pytest.raises(IntegrityError):
            # Use a UUID that doesn't exist in UnitOfMeasure
            non_existent_id = uuid.uuid4()
            with transaction.atomic():
                InventoryItem.objects.create(
                    name="Test Item",
                    unit_id=non_existent_id,  # This UUID doesn't exist in the database
                    quantity=10
                )

    def test_uuid_primary_keys(self):
        """Test that UUIDs are properly generated as primary keys."""
        # Create a unit and an item
        unit = UnitOfMeasure.objects.create(name="Test Unit", abbreviation="tu")
        item = InventoryItem.objects.create(name="Test Item", unit=unit, quantity=10)
        
        # Verify UUID was generated
        assert item.id is not None
        
        # Verify it's in the correct UUID format (length and type)
        assert len(str(item.id)) == 36  # Standard UUID string length
        assert "-" in str(item.id)  # UUID format includes hyphens
        
        # Verify they're different
        assert unit.id != item.id
        
        # Test that ID is a valid UUID
        assert isinstance(item.id, uuid.UUID)

    def test_description_can_be_null(self):
        """Test that description field in InventoryItem can be null."""
        # Create a unit
        unit = UnitOfMeasure.objects.create(name="Test Unit", abbreviation="tu")
        
        # Create an item with null description (should not raise an error)
        item = InventoryItem.objects.create(
            name="Test Item", 
            unit=unit, 
            quantity=10,
            description=None
        )
        
        assert item.description is None