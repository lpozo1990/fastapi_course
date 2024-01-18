from fastapi import FastAPI

app = FastAPI()


@app.get("/user/admin")
def admin():
    return {"this is admin page"}


@app.get("/user/{username}")
def profile(username):
    return {f"this is profile page for {username}"}


@app.get("/products")
def products(id=1, price=200):
    return {f"product with an id: {id} and ${price}"}


@app.get("/profile/{userid}/comments")
def profile(userid: int, commentid: int = 12):
    return {f"Profile page for user {userid} and commentid {commentid}"}
