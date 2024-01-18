from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "from snippet"


@app.get("/property/{id}")
def property(id):
    return f"this is a property page {id}"


@app.get("/movies")
def movies():
    return {"movi list": {"movie1", "movie2"}}
