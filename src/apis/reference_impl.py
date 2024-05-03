
from fastapi import FastAPI

# this code will serve a request and return a response asynchronously

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World from Omar"}


