from django.db import models

# Create your models here.
class Destination:
    id : int
    name : str
    desc : str
    price : int
    img : str
    offer : bool
    
    def __init__(self, name, desc, price, img, offer):
        self.name = name
        self.desc = desc
        self.price = price
        self.img = img
        self.offer = offer