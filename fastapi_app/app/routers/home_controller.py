"""Home controller"""
from fastapi import APIRouter


ROUTER = APIRouter(tags=["Home"])


@ROUTER.get("/", description="Home")
def home():
    """home route"""
    return {"Hello": "World"}
