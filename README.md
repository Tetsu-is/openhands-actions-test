# openhands-actions-test

## Project Structure

This project is a simple FastAPI application that follows a 3-layer architecture:

- `src/main.py`: Entry point for the FastAPI application
- `src/model.py`: Contains the domain model (Item class) and data persistence logic
- `src/view.py`: Defines request and response data structures
- `src/controller.py`: Handles HTTP requests and connects the model and view layers

## Setup

1. install `rye`
2. Run `rye sync`
3. Run `rye run uvicorn src.main:app --reload`

## Run tests

```bash
rye run pytest
```
