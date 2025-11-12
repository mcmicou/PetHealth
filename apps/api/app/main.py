from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="PetHealth API", version="0.1.0")

# Allow the Next.js dev server to call the API during development
origins = [
    "http://localhost:3000",    # Next.js default dev URL
    "http://127.0.0.1:3000",
    "http://localhost:3001",
    "http://127.0.0.1:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],   # GET, POST, etc.
    allow_headers=["*"],   # Authorization, Content-Type, etc.
)

@app.get("/health")
def health():
    return {"status": "ok", "service": "pethealth-api"}