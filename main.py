from typing import List, Set
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Profile(BaseModel):
    name: str = "Tom"
    email: str = "email@mail.com"
    age: int = 29


class Offer(BaseModel):
    name: str
    description: str
    price: float


class User(BaseModel):
    name: str = "placeholder"
    email: str = "mail@email.com"
    offerts: List[Offer]


class Product(BaseModel):
    name: str = Field(examples=["Foo"])
    description: str | None = Field(default=None, examples=["A very nice Item"])
    price: float = Field(examples=[35.4])
    discount: int
    discounted_price: float
    tags: Set[str] = []


@app.post("/purchase")
def purchase(product: Product):
    return {"product": product}
