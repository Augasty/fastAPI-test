from fastapi import FastAPI

app = FastAPI()

# endpoints
# GET - get an info
# POST - create something new
# PUT - update something that is already existing
# DELETE - delete something
@app.get("/")
def index():
    return {"name":"first data"}

# to run a firstapi project
# uvicorn myapi:app --reload
# to check the documentaiton for the APIs: the_url/docs



