from fastapi import FastAPI

app = FastAPI(title="AI-Assessor API")


@app.get("/health")
def health():
    return {"status": "ok"}