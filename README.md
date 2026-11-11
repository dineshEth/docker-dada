# Image Backend API

A simple FastAPI backend for image processing with a beautiful Docker-themed landing page.

## Preview

![Home Page Preview](screenshots/home-page.svg)

*The actual page has a full Docker-themed design with interactive features. Run the server and visit http://localhost:8000 to see it live.*

## Endpoints

- **GET /** - Root endpoint that returns a welcome message with Docker-themed UI
- **GET /health** - Health check endpoint that returns API status in JSON format

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
- UI templates are in the `templates/` directory for easy customization
