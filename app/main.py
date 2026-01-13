from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

MESSAGE = "Deployed via Argo CD GitOps 🚀"


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/", response_class=HTMLResponse)
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Argo CD GitOps Deployment</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                color: white;
                height: 100vh;
                margin: 0;
                display: flex;
                align-items: center;
                justify-content: center;
            }}
            .card {{
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 0 30px rgba(0,0,0,0.4);
                text-align: center;
                max-width: 600px;
            }}
            h1 {{
                font-size: 2.5em;
                margin-bottom: 10px;
            }}
            p {{
                font-size: 1.2em;
                opacity: 0.9;
            }}
            .status {{
                margin-top: 20px;
                padding: 10px;
                background: #00c853;
                border-radius: 8px;
                font-weight: bold;
                display: inline-block;
            }}
            footer {{
                margin-top: 30px;
                font-size: 0.9em;
                opacity: 0.7;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 GitOps Deployment Successful</h1>
            <p>{MESSAGE}</p>
            <div class="status">Application Status: Running</div>
            <footer>
                <br/>
                Managed by Argo CD • Powered by Kubernetes & FastAPI
            </footer>
        </div>
    </body>
    </html>
    """
