from django.urls import path
from inventory.views import (
    InventoryItemListView,
    InventoryItemDetailView,
    InventoryItemCreateView,
    InventoryItemUpdateView,
    InventoryItemDeleteView,
    UnitOfMeasureListView,
    UnitOfMeasureCreateView,
)

app_name = 'inventory'

urlpatterns = [
    # Inventory Item URLs
    path('', InventoryItemListView.as_view(), name='item-list'),
    path('items/<uuid:pk>/', InventoryItemDetailView.as_view(), name='item-detail'),
    path('items/create/', InventoryItemCreateView.as_view(), name='item-create'),
    path('items/<uuid:pk>/update/', InventoryItemUpdateView.as_view(), name='item-update'),
    path('items/<uuid:pk>/delete/', InventoryItemDeleteView.as_view(), name='item-delete'),
    
    # Unit of Measure URLs
    path('units/', UnitOfMeasureListView.as_view(), name='unit-list'),
    path('units/create/', UnitOfMeasureCreateView.as_view(), name='unit-create'),
]