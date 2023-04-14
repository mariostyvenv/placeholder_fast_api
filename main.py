import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/api/placeholder")
def hello():
    return {"Nombre: ": "<Su nombre>"}

@app.get("/api/placeholder/health_check")
def health_check():
    return {"status: ": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)