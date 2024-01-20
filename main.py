from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Profile(BaseModel):
    name: str = "Tom"
    email: str = "email@mail.com"
    age: int = 29


class Product(BaseModel):
    name: str
    price: int = Field(title="price of the item", description="This is descr")
    discount: int
    discounted_price: float


class User(BaseModel):
    name: str
    email: str


@app.post("/purchase")
def purchase(user: User, product: Product):
    return {"user": user, "product": product}
