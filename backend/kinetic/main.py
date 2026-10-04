from fastapi import FastAPI

app = FastAPI(title="Kinetic Studio Motion API", version="0.1.0")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "kinetic-studio-motion"}
