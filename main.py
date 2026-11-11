from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime, timezone
import time
from pathlib import Path

app = FastAPI(title="Image Backend API")
start_time = time.time()

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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
