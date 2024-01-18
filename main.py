from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Profile(BaseModel):
    name: str = "Tom"
    email: str = "email@mail.com"
    age: int = 29


@app.post("/adduser")
def addUser(user: Profile):
    return {f"user data:{user.model_dump()}"}
