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
    name: str
    price: int = Field(title="price of the item", description="This is descr")
    discount: int
    discounted_price: float
    tags: Set[str] = []
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Phone",
                    "price": 100,
                    "discount": 10,
                    "tags": ["tag1", "tag2"],
                }
            ]
        }
    }


@app.post("/purchase")
def purchase(product: Product):
    return {"product": product}
