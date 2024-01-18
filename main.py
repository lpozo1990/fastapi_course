from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Profile(BaseModel):
    name: str = "Tom"
    email: str = "email@mail.com"
    age: int = 29


class Product(BaseModel):
    name: str
    price: int
    discount: int
    discounted_price: float


@app.post("/adduser")
def addUser(user: Profile):
    return {f"user data:{user.model_dump()}"}


@app.post("/addproduct")
def add_product(product: Product):
    product.discounted_price = product.price - (product.price * product.discount) / 100
    return product
