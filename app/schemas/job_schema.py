from pydantic import BaseModel

class JobCreate(BaseModel):
    company: str
    role: str
    status: str
    location: str
