from fastapi import FastAPI

app = FastAPI(title="Image Backend API")


@app.get("/")
async def root():
    """Root endpoint for the image backend."""
    return {"message": "Welcome to the Image Backend API"}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "message": "API is running"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
