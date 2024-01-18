from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "from snippet"


@app.get("/property/{id}")
def property(id: int):
    return f"this is a property page {id}"


@app.get("/movies")
def movies():
    return {"movi list": {"movie1", "movie2"}}


@app.get("/profile/{username}")
def profile(username: str):
    return {f"this is the page for user {username}"}
