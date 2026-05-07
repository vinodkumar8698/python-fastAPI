from pydantic import BaseModel
class Product(BaseModel):
    id: int
    title:str
    desc: str
    price: float

class User(BaseModel):
    id: int
    name: str
    age: int
    product: Product







    