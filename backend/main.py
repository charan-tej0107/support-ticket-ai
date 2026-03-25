from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes import router

app = FastAPI()

# ✅ VERY IMPORTANT: allow ALL origins for hackathon
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include router AFTER middleware
app.include_router(router)

@app.get("/")
def root():
    return {"message": "API running 🚀"}