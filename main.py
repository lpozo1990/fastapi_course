from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "from snippet"


@app.get("/property")
def property():
    return "this is a property page"


@app.get("/movies")
def movies():
    return {"movi list": {"movie1", "movie2"}}
