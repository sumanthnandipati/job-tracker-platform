from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.auth.hash import hash_password, verify_password
from app.auth.jwt_handler import create_access_token, verify_token

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/login"
)

# ---------------------------
# REGISTER USER
# ---------------------------
@router.post("/register")
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }


# ---------------------------
# LOGIN USER
# ---------------------------
@router.post("/login")
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        User.username == form_data.username
    ).first()

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if not verify_password(
        form_data.password,
        existing_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    access_token = create_access_token(
        data={"sub": existing_user.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# ---------------------------
# PROTECTED ROUTE
# ---------------------------
@router.get("/profile")
def protected_route(
    token: str = Depends(oauth2_scheme)
):
    payload = verify_token(token)

    return {
        "message": "Protected route accessed",
        "user": payload
    }
