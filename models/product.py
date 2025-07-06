from sqlalchemy import *
from extentions import db

class Product(db.Model):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable = False, index= True)
    description = Column(String, nullable = False, index= True)
    price = Column(Integer,  nullable = False, index= True)
    active = Column(Integer,  nullable = False, index= True)
    # در بالا که نوشتیم اکتیو میخوایم موجود بودن محصول رو ببینیم با 0 و یک
   