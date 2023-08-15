from pydantic import BaseModel


class DefaultResponse(BaseModel):
    """Default Response schema class"""

    message: str
