from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.job import Job
from app.schemas.job_schema import JobCreate
from app.auth.dependencies import get_current_user
from app.models.user import User

router = APIRouter()


# =========================
# CREATE JOB
# =========================
@router.post("/jobs")
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_job = Job(
        company=job.company,
        role=job.role,
        status=job.status,
        location=job.location,
        user_id=current_user.id
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return {
        "message": "Job created successfully",
        "job_id": new_job.id
    }


# =========================
# GET ALL JOBS (PAGINATION)
# =========================
@router.get("/jobs")
def get_jobs(
    page: int = 1,
    limit: int = 5,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    skip = (page - 1) * limit

    jobs = db.query(Job).filter(
        Job.user_id == current_user.id
    ).offset(skip).limit(limit).all()

    return jobs


# =========================
# SEARCH JOBS BY COMPANY
# =========================
@router.get("/jobs/search")
def search_jobs(
    company: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    jobs = db.query(Job).filter(
        Job.user_id == current_user.id,
        Job.company.ilike(f"%{company}%")
    ).all()

    return jobs


# =========================
# FILTER JOBS BY STATUS
# =========================
@router.get("/jobs/filter")
def filter_jobs(
    status: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    jobs = db.query(Job).filter(
        Job.user_id == current_user.id,
        Job.status == status
    ).all()

    return jobs


# =========================
# GET SINGLE JOB
# =========================
@router.get("/jobs/{job_id}")
def get_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    job = db.query(Job).filter(
        Job.id == job_id,
        Job.user_id == current_user.id
    ).first()

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    return job


# =========================
# UPDATE JOB
# =========================
@router.put("/jobs/{job_id}")
def update_job(
    job_id: int,
    job_data: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    job = db.query(Job).filter(
        Job.id == job_id,
        Job.user_id == current_user.id
    ).first()

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    job.company = job_data.company
    job.role = job_data.role
    job.status = job_data.status
    job.location = job_data.location

    db.commit()
    db.refresh(job)

    return {
        "message": "Job updated successfully"
    }


# =========================
# DELETE JOB
# =========================
@router.delete("/jobs/{job_id}")
def delete_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    job = db.query(Job).filter(
        Job.id == job_id,
        Job.user_id == current_user.id
    ).first()

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    db.delete(job)
    db.commit()

    return {
        "message": "Job deleted successfully"
    }


# =========================
# DASHBOARD ANALYTICS
# =========================
@router.get("/dashboard/analytics")
def get_dashboard_analytics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    total_jobs = db.query(Job).filter(
        Job.user_id == current_user.id
    ).count()

    applied = db.query(Job).filter(
        Job.user_id == current_user.id,
        Job.status == "Applied"
    ).count()

    interview = db.query(Job).filter(
        Job.user_id == current_user.id,
        Job.status == "Interview"
    ).count()

    rejected = db.query(Job).filter(
        Job.user_id == current_user.id,
        Job.status == "Rejected"
    ).count()

    offer = db.query(Job).filter(
        Job.user_id == current_user.id,
        Job.status == "Offer"
    ).count()

    return {
        "total_jobs": total_jobs,
        "applied": applied,
        "interview": interview,
        "rejected": rejected,
        "offer": offer
    }