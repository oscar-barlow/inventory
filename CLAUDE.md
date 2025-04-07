# Claude Code Guide

## Commands to Run Before Making Changes

When working with this project, these are the key commands to run:

```bash
# Run tests in watch mode (automatically runs tests when files change)
make test-watch

# Start the development server
make run

# Apply migrations
make migrate
```

## Project Structure

- Models are in `inventory/models/` directory
- Views are in `inventory/views/` directory
- Templates are in `inventory/templates/inventory/`

## Importing Conventions

Always use fully qualified imports, for example:

```python
from inventory.models.unit_of_measure import UnitOfMeasure
from inventory.models.inventory_item import InventoryItem
```

## Development Workflow

1. Run `make test-watch` in a terminal to automatically run tests when files change
2. Make your code changes
3. Tests will run automatically when you save files
4. Once tests pass, verify changes with `make run` to start the server