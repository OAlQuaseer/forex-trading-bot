from fastapi import FastAPI, Path, Request
from fastapi.responses import JSONResponse

from services import web_scraping_service
from models import MyException, Configuration, Index

smart_data_science_app = FastAPI(title='SMART Data Science Application',
              description='A Smart Data Science Application running on FastAPI + uvicorn',
              version='0.0.1')

@smart_data_science_app.get("/{index}")
async def get_result(index: Index = Path(..., title="The name of the Index")):
    config = Configuration(index=index)
    try:
        result = await web_scraping_service.run(config)
        return JSONResponse(status_code=200, content=result)
    except Exception as e:
        raise MyException(e)
    
@smart_data_science_app.exception_handler(MyException)
async def unicorn_exception_handler(request: Request, exc: MyException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Error occurred! Please contact the system admin."},
    )