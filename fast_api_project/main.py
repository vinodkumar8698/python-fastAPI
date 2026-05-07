from fastapi import FastAPI
from models import Product
app = FastAPI()

@app.get("/")
def greet():
    return "Hello, FastAPI!"


products = [
    Product(id=1, title="Iphone 17", desc="this is iphone 17", price=890, qty=20),
    Product(id=2, title="Iphone 15", desc="this is iphone 15", price=690, qty=20),
    Product(id=3, title="Iphone 16", desc="this is iphone 16", price=790, qty=20)
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id:int):
    for p in products:
        if p.id == id:
            return p
    return "There is No Product found" 