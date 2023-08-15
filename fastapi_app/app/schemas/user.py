from pydantic import BaseModel


class User(BaseModel):
    """User schema class"""

    id: int
    name: str
    email: str
    password: str
    is_active: bool
