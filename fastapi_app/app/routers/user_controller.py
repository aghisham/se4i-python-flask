"""User controller"""
from fastapi import APIRouter
from app.schemas.user import User as UserSchema
from app.schemas.default import DefaultResponse
from app.models.user import User
from app.db import DB


ROUTER = APIRouter(prefix="/user", tags=["Users"])


@ROUTER.get("/", description="Get all users")
async def index(skip: int = 0, limit: int = 10):
    """Get all users"""
    return DB.query(User).offset(skip).limit(limit).all()


@ROUTER.get("/{user_id}", description="Get user", response_model=UserSchema)
async def show(user_id: int):
    """Get user"""
    return DB.query(User).filter(User.id == user_id).first()


@ROUTER.put("/{user_id}", description="Update user", response_model=DefaultResponse)
async def update(user_id: int):
    """Update user"""
    try:
        user = DB.query(User).filter(User.id == user_id).first()
        return {"message": "Fuccess"}
    except Exception:
        return {"message": "Failed"}


@ROUTER.post("/", description="Create user", response_model=DefaultResponse)
async def create(user: UserSchema):
    """Create user"""
    try:
        new_user = User(name=user.name, email=user.email,
                        password=user.password)
        DB.add(new_user)
        DB.commit()
        DB.refresh(new_user)
        return {"message": "Fuccess"}
    except Exception:
        return {"message": "Failed"}
