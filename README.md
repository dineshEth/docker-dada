# Image Backend API

A simple FastAPI backend for image processing.

## Endpoints

- **GET /** - Root endpoint that returns a welcome message
- **GET /health** - Health check endpoint that returns API status

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

3. Open http://localhost:8000 in your browser or use a tool like curl:
   ```bash
   curl http://localhost:8000/
   curl http://localhost:8000/health
   ```

## Development

- The server will reload automatically during development when using `--reload` flag
- FastAPI provides automatic interactive API documentation at http://localhost:8000/docs
