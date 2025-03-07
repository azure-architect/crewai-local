from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="CrewAI Local API",
    description="API for running CrewAI locally",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "CrewAI Local API is running"}


@app.get("/health")
async def health_check():
    return {"status": "banging and hanging in there baby 🤙"}