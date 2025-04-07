# Home Inventory Management System

A simple web application to manage your home inventory using Django and SQLite.

## Features

- Track inventory items with quantities and units of measure
- CRUD operations for both inventory items and units of measure
- Responsive UI using Bootstrap

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd inventory
   ```

2. Install dependencies using Poetry:
   ```
   poetry install
   ```

3. Set up the database and initial data:
   ```
   make setup
   ```

4. Start the development server:
   ```
   make run
   ```

5. Access the application at http://127.0.0.1:8000

## Usage

- **Inventory Items**: Add, edit, view, and delete inventory items at the main page
- **Units of Measure**: Manage units of measure at http://127.0.0.1:8000/units/

## Development

- Make database migrations:
  ```
  make makemigrations
  ```

- Apply migrations:
  ```
  make migrate
  ```

- Initialize sample data:
  ```
  make init-data
  ```

- Run tests:
  ```
  make test
  ```

- Run smoke test (applies migrations and verifies app starts):
  ```
  make smoke-test
  ```
  
- Watch for changes and run tests automatically:
  ```
  make test-watch
  ```

## Project Structure

- `inventory/`: Main application code
  - `models/`: Database models for inventory items and units
  - `views/`: View classes for handling HTTP requests
  - `templates/`: HTML templates for rendering UI
- `config/`: Project settings and configuration
- `tests/`: Test files
  - `test_smoke.py`: Smoke test that verifies migrations apply and the app starts