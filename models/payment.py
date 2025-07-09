from sqlalchemy import *
from extentions import db

class Payment(db.Model):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    status = Column(String, default="pending")
    cart_id = Column(Integer, ForeignKey('carts.id', nullable = False))
    # usersهمون اسم جدوله!
    cart = db.relationship('Cart', backref = 'payments')
    # ارتباط یک به چند ( هر سبد خرید چند درگاه پرداخت داره)