# forex-trading-bot


# to build an image: docker build --tag forex-trading-bot-image .
# to run a container: docker run -ti --rm -p 127.0.0.1:3000:3000 forex-trading-bot-image

# check OS information on Linux: lsb_release -a



# to run the APIs server: uvicorn src.apis.api_reference_impl:app --reload

# APIs documentation:  http://127.0.0.1:8000/redoc, http://127.0.0.1:8000/doc 