from sqlalchemy import *
from extentions import db , get_current_time

class Payment(db.Model):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    status = Column(String, default="pending")
    price = Column(Integer)
    token = Column(String)
    refid = Column(String)
    card_pan = Column(String)
    transaction_id = Column(Integer)
    date_created = Column(String(15), default = get_current_time)
    cart_id = Column(Integer, ForeignKey('carts.id'), nullable = False)
    # usersهمون اسم جدوله!
    cart = db.relationship('Cart', backref = 'payments')
    # ارتباط یک به چند ( هر سبد خرید چند درگاه پرداخت داره)


    def get_status_persian(self):
        if self.status == 'pending':
            return "در انتظار پرداخت"
        
        if self.status == 'success':
            return "پرداخت شده"

        if self.status == 'failed':
            return "عدم موفقیت"
