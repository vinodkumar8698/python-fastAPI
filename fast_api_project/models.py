from pydantic import BaseModel
class Product(BaseModel):
    id: int
    title:str
    desc: str
    price: float
    qty: int

    # def __init__(self, id:int, title:str, desc: str, price:float, qty:int):
    #     self.id = id
    #     self.title = title
    #     self.desc = desc
    #     self.price = price
    #     self.qty = qty







    