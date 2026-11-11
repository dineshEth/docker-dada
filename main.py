from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime, timezone
import time
from pathlib import Path
from redis.asyncio import Redis

app = FastAPI(title="Image Backend API")
start_time = time.time()

# Redis client for persistent counter
redis = Redis(host="localhost", port=6379, db=0)

# Serve static files from public directory
app.mount("/public", StaticFiles(directory="public"), name="public")

# Load HTML template from file
TEMPLATES_DIR = Path(__file__).parent / "templates"
INDEX_HTML = (TEMPLATES_DIR / "index.html").read_text()


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the home page."""
    return INDEX_HTML


@app.get("/health")
async def health_check():
    """Health check endpoint with timestamp and system status."""
    now = datetime.now(timezone.utc)
    timestamp = now.isoformat()
    
    uptime_seconds = time.time() - start_time
    uptime_str = f"{int(uptime_seconds // 3600)}h {int((uptime_seconds % 3600) // 60)}m {int(uptime_seconds % 60)}s"
    
    return {
        "status": "healthy",
        "message": "API is running",
        "timestamp": timestamp,
        "uptime": uptime_str,
        "version": "1.0.0",
        "service": "Image Backend API"
    }


@app.post("/counter")
async def increment_counter():
    """POST endpoint that increments a global hit counter by 1.
    
    Uses Redis to persist the counter value across server restarts.
    Returns the current counter value along with a UTC timestamp and metadata.
    Each call to this endpoint increases the counter sequentially.
    """
    counter = await redis.incr("hit_counter")
    now = datetime.now(timezone.utc)
    return {
        "counter": counter,
        "timestamp": now.isoformat(),
        "description": "Global request counter incremented by 1 (persisted in Redis)",
        "endpoint": "/counter",
        "method": "POST",
        "increment_by": 1,
        "storage": "redis"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
