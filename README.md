# openhands-actions-test

A simple FastAPI server application with a 3-layer architecture.

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

- **Main Application** (`src/main.py`): Entry point that configures and starts the FastAPI application

## Setup

1. install `rye`
2. Run `rye sync`
3. Run `rye run uvicorn src.main:app --reload`

## Run tests

```bash
rye run pytest
```

## API Endpoints

- `POST /items/`: Create a new item
  - Request body: `{"name": "item_name"}`
  - Response: `{"message": "Item added", "item": "item_name"}`

- `GET /items/`: Get all items
  - Response: `{"items": ["item1", "item2", ...]}`
