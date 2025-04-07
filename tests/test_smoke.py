import os
import subprocess
import time
import pytest
import requests
from django.core.management import call_command
from django.db.migrations.executor import MigrationExecutor
from django.db import connections, DEFAULT_DB_ALIAS


@pytest.mark.django_db(transaction=True)
def test_migrations_apply():
    """Test that migrations apply without error"""
    # Get the database connection
    connection = connections[DEFAULT_DB_ALIAS]
    
    # Get the migration executor
    executor = MigrationExecutor(connection)
    
    # Get the current migration state
    executor.loader.build_graph()
    
    # Apply all migrations
    call_command('migrate')
    
    # Verify models can be imported
    from inventory.models import InventoryItem, UnitOfMeasure
    
    # Create test data
    unit = UnitOfMeasure.objects.create(name="Test Unit", abbreviation="tu")
    item = InventoryItem.objects.create(
        name="Test Item",
        description="Test Description",
        unit=unit,
        quantity=10.5
    )
    
    # Verify data was created correctly
    assert UnitOfMeasure.objects.count() == 1
    assert InventoryItem.objects.count() == 1
    assert item.unit == unit
    assert item.quantity == 10.5


@pytest.fixture(scope="module")
def django_server():
    """Fixture to start and stop the Django development server"""
    # Start the development server on port 8123
    server_process = subprocess.Popen(
        ["python", "manage.py", "runserver", "127.0.0.1:8123", "--noreload"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    )
    
    # Wait for the server to start
    time.sleep(3)
    
    yield server_process
    
    # Stop the server
    server_process.terminate()
    server_process.wait()


def test_server_starts(django_server):
    """Test that the server starts and returns a 200 response"""
    # Test the main page
    response = requests.get("http://127.0.0.1:8123/")
    assert response.status_code == 200
    
    # Test the units endpoint
    response = requests.get("http://127.0.0.1:8123/units/")
    assert response.status_code == 200