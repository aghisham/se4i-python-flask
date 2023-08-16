"""Home controller"""
from fastapi import APIRouter


ROUTER = APIRouter()


@ROUTER.get("/", description="Home")
def home():
    """home route"""
    return {"Hello": "World"}
