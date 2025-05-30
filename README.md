# openhands-actions-test

A simple FastAPI server application with a 3-layer architecture and HTML templates.

## Project Structure

The application follows a 3-layer architecture:

- **Model Layer** (`src/model.py`): Defines the domain model and data persistence logic
  - `Item` class: Manages the item data and provides methods for CRUD operations

- **View Layer** (`src/view.py`): Defines the data structures for requests and responses
  - Request models: Define the structure of incoming data
  - Response models: Define the structure of outgoing data

- **Controller Layer** (`src/controller.py`): Handles HTTP requests and orchestrates the application flow
  - Routes HTTP requests to appropriate handlers
  - Uses the model layer for data operations
  - Uses the view layer for data transformation

- **Templates** (`src/templates/`): HTML templates using Jinja2
  - `base.html`: Base template with common layout and styling
  - `item_list.html`: Template for displaying the list of items
  - `item_create.html`: Template for the item creation form

- **Main Application** (`src/main.py`): Entry point that configures and starts the FastAPI application

## Setup

1. install `rye`
2. Run `rye sync`
3. Run `rye run uvicorn src.main:app --reload`

## Run tests

```bash
rye run pytest
```

## Endpoints

### API Endpoints

- `POST /api/items/`: Create a new item via API
  - Request body: `{"name": "item_name"}`
  - Response: `{"message": "Item added", "item": "item_name"}`

- `GET /api/items/`: Get all items via API
  - Response: `{"items": ["item1", "item2", ...]}`

### HTML Endpoints

- `GET /`: Redirects to the items list page

- `GET /items`: Display the list of all items
  - Renders the `item_list.html` template

- `GET /items/create`: Display the item creation form
  - Renders the `item_create.html` template

- `POST /items/`: Process the item creation form submission
  - Redirects to `/items` after successful creation
