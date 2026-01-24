from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any

app = FastAPI()

# ✅ Allow frontend (React) to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/generate_script")
async def generate_script(payload: Dict[str, Any]):
    print("📥 Received DAG payload:")
    print(payload)

    return {
        "status": "success"
    }
