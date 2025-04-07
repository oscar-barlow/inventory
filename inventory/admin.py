from django.contrib import admin
from inventory.models import UnitOfMeasure, InventoryItem

@admin.register(UnitOfMeasure)
class UnitOfMeasureAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation')
    search_fields = ('name', 'abbreviation')

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit', 'created_at', 'updated_at')
    list_filter = ('unit',)
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
