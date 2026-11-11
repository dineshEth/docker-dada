from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime, timezone
import time

app = FastAPI(title="Image Backend API")
start_time = time.time()


@app.get("/", response_class=HTMLResponse)
async def root():
    return """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Docker | Image Backend</title>

            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

            <style>
                :root {
                    --primary: #a7c957;
                    --accent: #affc41;
                    --light: #b2ff9e;
                    --mint: #1dd3b0;
                    --dark: #386641;
                    --background: #101810;
                    --surface: #172319;
                    --text: #f1f8ed;
                    --muted: #a5b5a2;
                }

                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }

                body {
                    font-family: 'Inter', sans-serif;
                    background: var(--background);
                    color: var(--text);
                    line-height: 1.6;
                }

                a {
                    text-decoration: none;
                    color: inherit;
                }

                .navbar {
                    height: 80px;
                    padding: 0 8%;
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    border-bottom: 1px solid #ffffff12;
                    background: #101810eF;
                }

                .logo {
                    font-size: 25px;
                    font-weight: 900;
                    color: var(--primary);
                    letter-spacing: -1px;
                }

                .logo span {
                    color: white;
                }

                .nav-links {
                    display: flex;
                    gap: 32px;
                    color: var(--muted);
                    font-size: 14px;
                }

                .nav-links a:hover {
                    color: var(--accent);
                }

                .status {
                    color: var(--mint);
                    font-size: 13px;
                    font-weight: 700;
                }

                .status::before {
                    content: "";
                    display: inline-block;
                    width: 8px;
                    height: 8px;
                    background: var(--mint);
                    border-radius: 50%;
                    margin-right: 8px;
                    box-shadow: 0 0 12px var(--mint);
                }

                .hero {
                    min-height: 570px;
                    padding: 100px 8%;
                    display: grid;
                    grid-template-columns: 1.2fr 0.8fr;
                    align-items: center;
                    gap: 60px;
                    background:
                        radial-gradient(ellipse at 85% 40%, #38664155, transparent 50%),
                        radial-gradient(ellipse at 10% 90%, #a7c95715, transparent 40%);
                }

                .tag {
                    display: inline-block;
                    padding: 8px 15px;
                    border: 1px solid #a7c95755;
                    border-radius: 30px;
                    color: var(--accent);
                    font-size: 12px;
                    font-weight: 700;
                    letter-spacing: 1px;
                    margin-bottom: 25px;
                }

                .hero h1 {
                    font-size: clamp(42px, 6vw, 72px);
                    line-height: 1.08;
                    letter-spacing: -3px;
                    font-weight: 900;
                    margin-bottom: 25px;
                }

                .hero h1 span {
                    color: var(--primary);
                }

                .hero p {
                    color: var(--muted);
                    font-size: 17px;
                    max-width: 560px;
                    margin-bottom: 35px;
                }

                .buttons {
                    display: flex;
                    gap: 15px;
                    flex-wrap: wrap;
                }

                .btn {
                    padding: 14px 25px;
                    border-radius: 9px;
                    font-weight: 700;
                    font-size: 14px;
                    transition: .25s;
                }

                .btn-primary {
                    background: var(--primary);
                    color: #172319;
                }

                .btn-primary:hover {
                    background: var(--accent);
                    transform: translateY(-3px);
                }

                .btn-outline {
                    border: 1px solid #ffffff30;
                    color: white;
                }

                .btn-outline:hover {
                    border-color: var(--mint);
                    color: var(--mint);
                }

                .visual {
                    background: linear-gradient(145deg, #263c29, #172319);
                    border: 1px solid #a7c95730;
                    border-radius: 25px;
                    padding: 35px;
                    box-shadow: 0 30px 80px #00000050;
                }

                .docker-icon {
                    font-size: 90px;
                    text-align: center;
                    margin-bottom: 20px;
                }

                .terminal {
                    background: #0b120d;
                    border-radius: 12px;
                    padding: 22px;
                    font-family: monospace;
                    font-size: 13px;
                    overflow-wrap: anywhere;
                }

                .terminal-header {
                    color: var(--muted);
                    margin-bottom: 20px;
                }

                .terminal p {
                    margin: 9px 0;
                    color: var(--light);
                }

                .terminal .green {
                    color: var(--mint);
                }

                .section {
                    padding: 95px 8%;
                }

                .section-heading {
                    text-align: center;
                    max-width: 650px;
                    margin: 0 auto 55px;
                }

                .section-heading small {
                    color: var(--primary);
                    text-transform: uppercase;
                    font-weight: 800;
                    letter-spacing: 2px;
                }

                .section-heading h2 {
                    font-size: 38px;
                    letter-spacing: -1.5px;
                    margin: 12px 0;
                }

                .section-heading p {
                    color: var(--muted);
                }

                .cards {
                    display: grid;
                    grid-template-columns: repeat(3, 1fr);
                    gap: 22px;
                }

                .card {
                    background: var(--surface);
                    border: 1px solid #ffffff12;
                    padding: 30px;
                    border-radius: 17px;
                    transition: .3s;
                }

                .card:hover {
                    transform: translateY(-7px);
                    border-color: var(--primary);
                    background: #1d3021;
                }

                .card-icon {
                    font-size: 32px;
                    margin-bottom: 20px;
                }

                .card h3 {
                    margin-bottom: 12px;
                    font-size: 19px;
                }

                .card p {
                    color: var(--muted);
                    font-size: 14px;
                }

                .about {
                    background: #172319;
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    align-items: center;
                    gap: 70px;
                }

                .about h2 {
                    font-size: 42px;
                    line-height: 1.2;
                    margin: 15px 0 20px;
                }

                .about p {
                    color: var(--muted);
                    margin-bottom: 18px;
                }

                .architecture {
                    background: #101810;
                    padding: 30px;
                    border: 1px solid #a7c95730;
                    border-radius: 18px;
                }

                .architecture h3 {
                    color: var(--primary);
                    margin-bottom: 20px;
                }

                .layer {
                    padding: 18px;
                    text-align: center;
                    margin: 12px 0;
                    border-radius: 9px;
                    background: #263c29;
                    border: 1px solid #a7c95735;
                    font-weight: 700;
                }

                .layer.highlight {
                    background: var(--dark);
                    color: var(--light);
                    border-color: var(--primary);
                }

                .arrow {
                    text-align: center;
                    color: var(--mint);
                    font-size: 22px;
                }

                .api-section {
                    text-align: center;
                    padding: 85px 8%;
                    background: linear-gradient(135deg, #386641, #172319);
                }

                .api-section h2 {
                    font-size: 38px;
                    margin-bottom: 15px;
                }

                .api-section p {
                    color: #d4e6d0;
                    margin-bottom: 30px;
                }

                .footer {
                    padding: 30px 8%;
                    display: flex;
                    justify-content: space-between;
                    flex-wrap: wrap;
                    gap: 15px;
                    color: var(--muted);
                    font-size: 13px;
                    border-top: 1px solid #ffffff12;
                }

                .footer strong {
                    color: var(--primary);
                }

                @media(max-width: 800px) {
                    .hero, .about {
                        grid-template-columns: 1fr;
                    }

                    .hero {
                        padding-top: 70px;
                    }

                    .cards {
                        grid-template-columns: 1fr;
                    }

                    .nav-links {
                        display: none;
                    }

                    .section-heading h2,
                    .about h2 {
                        font-size: 30px;
                    }
                }
            </style>
        </head>

        <body>

            <nav class="navbar">
                <a href="/" class="logo">DOCKER<span>.</span></a>

                <div class="nav-links">
                    <a href="#home">Home</a>
                    <a href="#features">Features</a>
                    <a href="#about">About Docker</a>
                    <a href="/docs">API Docs</a>
                </div>

                <div class="status">API Online</div>
            </nav>

            <main>
                <section class="hero" id="home">
                    <div>
                        <div class="tag">✦ CONTAINERIZED IMAGE BACKEND</div>

                        <h1>
                            Build once.<br>
                            <span>Run anywhere.</span>
                        </h1>

                        <p>
                            Welcome to your Image Backend API. Powered by Docker,
                            built for consistency, scalability, and modern
                            application development. Simplify deployment and
                            ship your applications with confidence.
                        </p>

                        <div class="buttons">
                            <a href="/docs" class="btn btn-primary">
                                Explore API Docs →
                            </a>

                            <a href="#about" class="btn btn-outline">
                                Discover Docker
                            </a>
                        </div>
                    </div>

                    <div class="visual">
                        <div class="docker-icon">🐳</div>

                        <div class="terminal">
                            <div class="terminal-header">
                                ● ● ● &nbsp; image-backend ~ terminal
                            </div>

                            <p><span class="green">$</span> docker build -t image-api .</p>
                            <p>Building Docker image...</p>
                            <p class="green">✓ Image built successfully</p>
                            <p><span class="green">$</span> docker run -p 8000:8000 image-api</p>
                            <p class="green">✓ Application running</p>
                            <p>Server: http://localhost:8000</p>
                        </div>
                    </div>
                </section>

                <section class="section" id="features">
                    <div class="section-heading">
                        <small>Why Docker?</small>
                        <h2>Everything you need to ship faster.</h2>
                        <p>
                            A consistent development and deployment experience
                            from your local machine to production.
                        </p>
                    </div>

                    <div class="cards">
                        <div class="card">
                            <div class="card-icon">📦</div>
                            <h3>Containerization</h3>
                            <p>
                                Package your application, dependencies, and
                                configuration into portable containers.
                            </p>
                        </div>

                        <div class="card">
                            <div class="card-icon">⚡</div>
                            <h3>Fast Deployment</h3>
                            <p>
                                Build, ship, and launch applications quickly
                                with reproducible Docker images.
                            </p>
                        </div>

                        <div class="card">
                            <div class="card-icon">🔒</div>
                            <h3>Isolation</h3>
                            <p>
                                Run applications in isolated environments
                                with their own dependencies and processes.
                            </p>
                        </div>

                        <div class="card">
                            <div class="card-icon">🌍</div>
                            <h3>Portability</h3>
                            <p>
                                Run your containers across different
                                environments without configuration surprises.
                            </p>
                        </div>

                        <div class="card">
                            <div class="card-icon">📈</div>
                            <h3>Scalability</h3>
                            <p>
                                Make it easier to replicate application
                                instances as your workload grows.
                            </p>
                        </div>

                        <div class="card">
                            <div class="card-icon">🛠️</div>
                            <h3>Developer Friendly</h3>
                            <p>
                                Simplify workflows using Dockerfiles,
                                images, containers, and Docker Compose.
                            </p>
                        </div>
                    </div>
                </section>

                <section class="section about" id="about">
                    <div>
                        <small style="color:var(--primary);font-weight:800;">
                            UNDERSTANDING DOCKER
                        </small>

                        <h2>
                            What is <span style="color:var(--primary)">Docker?</span>
                        </h2>

                        <p>
                            Docker is a platform that allows developers to
                            package applications and their dependencies into
                            lightweight, portable units called containers.
                        </p>

                        <p>
                            Unlike traditional virtual machines, containers
                            share the host operating system kernel, making
                            them efficient and quick to start.
                        </p>

                        <p>
                            Whether you're developing an API, processing images,
                            or deploying a large application, Docker helps
                            ensure your software runs consistently everywhere.
                        </p>

                        <a href="https://docs.docker.com/"
                        target="_blank"
                        rel="noopener noreferrer"
                        class="btn btn-primary">
                            Learn Docker →
                        </a>
                    </div>

                    <div class="architecture">
                        <h3>Docker Architecture</h3>

                        <div class="layer">🐳 Docker Client</div>
                        <div class="arrow">↓</div>
                        <div class="layer">⚙️ Docker Engine</div>
                        <div class="arrow">↓</div>
                        <div class="layer highlight">📦 Docker Images</div>
                        <div class="arrow">↓</div>
                        <div class="layer highlight">🚀 Running Containers</div>
                        <div class="arrow">↓</div>
                        <div class="layer">🌐 Your Application</div>
                    </div>
                </section>

                <section class="api-section">
                    <h2>Your API. Ready to go.</h2>

                    <p>
                        Your image backend is powered by FastAPI.
                        Explore available endpoints and start building.
                    </p>

                    <a href="/docs" class="btn btn-primary">
                        Open Swagger Documentation →
                    </a>
                </section>
            </main>

            <footer class="footer">
                <div>© 2026 <strong>Image Backend API</strong></div>
                <div>Built with ❤️ using FastAPI & Docker</div>
                <div>Powered by <strong>Containers</strong></div>
            </footer>

        </body>
        </html>
            """

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
