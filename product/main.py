from fastapi import Depends, FastAPI

from product.schemas import Product
from . import models
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/product")
def add(request: Product, db: Session = Depends(get_db)):
    db_product = models.Product(**request.model_dump())
    db.add(db_product)
    db.commit()
    return request
