"""User controller"""
from app import app
from app.schemas.user import User
from app.schemas.default import DefaultResponse


@app.get("/user", description="Get all users", tags=["Users"])
def index(limit: int = 10):
    """Get all users"""
    return [{"Hello": "World"}]


@app.get("/user/{user_id}", description="Get user", tags=["Users"], response_model=User)
def show(user_id: int):
    """Get user"""
    return {"Hello": "World"}


@app.put("/user/{user_id}", description="Update user", tags=["Users"], response_model=DefaultResponse)
def update(user_id: int):
    """Update user"""
    try:
        return {"message": "Fuccess"}
    except Exception:
        return {"message": "Failed"}


@app.post("/user", description="Create user", tags=["Users"], response_model=DefaultResponse)
def create(user: User):
    """Create user"""
    try:
        return {"message": "Fuccess"}
    except Exception:
        return {"message": "Failed"}
