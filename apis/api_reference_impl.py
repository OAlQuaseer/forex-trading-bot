
from fastapi import FastAPI

# api_reference_impl.py


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


