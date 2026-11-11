# Image Backend API

A simple FastAPI backend for image processing with a beautiful Docker-themed landing page.

## Preview

![Home Page Preview](screenshots/home-page.svg)

*The actual page has a full Docker-themed design with interactive features. Run the server and visit http://localhost:8000 to see it live.*

## Quick Start with Docker (Recommended)

The easiest way to run this application is with Docker:

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) installed on your system

### Option 1: Using Docker Compose
```bash
# Build and run the container
docker-compose up -d --build

# View logs
docker-compose logs -f

# Access the application
# http://localhost:8000

# Stop the container
docker-compose down
```

### Option 2: Using Docker directly
```bash
# Build the image
docker build -t image-backend-api .

# Run the container
docker run -d -p 8000:8000 --name image-backend image-backend-api

# Access the application
# http://localhost:8000

# Stop the container
docker stop image-backend && docker rm image-backend
```

## Development Setup (Without Docker)

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

## Endpoints

- **GET /** - Root endpoint that returns a welcome message with Docker-themed UI
- **GET /health** - Health check endpoint that returns API status in JSON format

## Development Notes

- The server will reload automatically during development when using `--reload` flag
- FastAPI provides automatic interactive API documentation at http://localhost:8000/docs
- UI templates are in the `templates/` directory for easy customization
- For Docker development with auto-reload, uncomment the `--reload` flag in docker-compose.yml
