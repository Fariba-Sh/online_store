from sqlalchemy import *
from extentions import db
from sqlalchemy.orm import backref

class Cart(db.Model):
    __tablename__ = "carts"
    id = Column(Integer, primary_key=True)
    status = Column(String, default="pending")
    user_id = Column(Integer, ForeignKey('users.id'), nullable = False)
    # usersهمون اسم جدوله!
    user = db.relationship('User', backref = backref ('carts', lazy= 'dynamic'))
    # ارتباط یک به چند( هر کاربر چند سبد خرید میتونه داشته باشه)
    # lazy = 'dynamic' returns as query


    def total_price(self):
        total = 0
        for item in self.cart_items:
            t = item.price * item.quantity
            total += t
        return total
    

    def get_status_persian(self):
        if self.status == 'pending':
            return "در انتظار پرداخت"
        
        if self.status == 'paid':
            return "پرداخت شده"

        if self.status == 'sent':
            return "ارسال شده"

        if self.status == 'rejected':
            return "رد شده"
