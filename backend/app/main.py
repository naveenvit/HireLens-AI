from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import resume, analysis

# ✅ CREATE APP (ONLY ONCE)
app = FastAPI(
    title="AI Resume Analyzer API",
    version="1.0.0"
)

# ✅ ADD CORS (IMMEDIATELY AFTER APP CREATION)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://hirelens-ai.netlify.app",  # ✅ ADD THIS
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ REGISTER ROUTERS
app.include_router(resume.router)
app.include_router(analysis.router)

# ✅ HEALTH CHECK
@app.get("/")
def health_check():
    return {"status": "Backend running 🚀"}
