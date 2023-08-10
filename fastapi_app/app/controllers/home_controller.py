from app import app


@app.get("/", description="Home", tags=["Home"])
def home():
    """home route"""
    return {"Hello": "World"}
