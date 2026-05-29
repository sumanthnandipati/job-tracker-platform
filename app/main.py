from fastapi import FastAPI

from app.database.database import engine, Base

from app.routes.user_routes import router as user_router
from app.routes.job_routes import router as job_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)
app.include_router(job_router)

@app.get("/")
def home():
    return {
        "message": "Job Tracker API Running"
    }
