from fastapi import FastAPI
from models import Product, User
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
    return f"There is no product found with id {id}" 

@app.get("/user")
def get_user(user_id:int = None,name: str = "Guest", age: int = 0):
    return {"user_id": user_id, "name": name, "age": age}

@app.get("/search_product")
def search_product(id:int = 0, title: str = None, price: int = 0):
    return {"id": id, "title": title, "price": price}

# post method

@app.post("/user")
def create_user(user:User):
    return {
        "message": "User created successfully",
        "status": "success",
        "data": user
    }

