from typing import Set
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Profile(BaseModel):
    name: str = "Tom"
    email: str = "email@mail.com"
    age: int = 29


class User(BaseModel):
    name: str = "placeholder"
    email: str = "mail@email.com"


class Product(BaseModel):
    name: str
    price: int = Field(title="price of the item", description="This is descr")
    discount: int
    discounted_price: float
    tags: Set["User"] = []


@app.post("/purchase")
def purchase(user: User, product: Product):
    return {"user": user, "product": product}
