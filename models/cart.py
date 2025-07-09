from sqlalchemy import *
from extentions import db

class Cart(db.Model):
    __tablename__ = "carts"
    id = Column(Integer, primary_key=True)
    status = Column(String, default="pending")
    user_id = Column(Integer, ForeignKey('users.id', nullable = False))
    # usersهمون اسم جدوله!
    user = db.relationship('User', backref = 'carts')
    # ارتباط یک به چند( هر کاربر چند سبد خرید میتونه داشته باشه)