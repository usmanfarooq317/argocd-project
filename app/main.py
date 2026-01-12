from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Deployed via Argo CD GitOps 🚀"}

@app.get("/health")
def health():
    return {"status": "healthy"}
