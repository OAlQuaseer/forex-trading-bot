import uvicorn

from apis import smart_data_science_app
from apis import app






if __name__ == "__main__":

    uvicorn.run('apis.smart_data_science:smart_data_science_app', host="127.0.0.1", port=5000, log_level="info", reload=True)