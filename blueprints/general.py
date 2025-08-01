from flask import Blueprint, render_template,request
from models.product import Product
from sqlalchemy import func


app = Blueprint("general", __name__)

@app.route('/')
def main():
    search = request.args.get('search',None)

    products = Product.query.filter(Product.active == 1)

    if search != None:
        products = products.filter(Product.name.like(f'%{search}%'))

    products = products.order_by(Product.price.desc()).all()

    return render_template("main.html" , products = products , search = search)


@app.route('/products/<int:id>/<name>')
def product(id,name):
    product = Product.query.filter(Product.id == id).filter(Product.name == name).filter(Product.active == 1).first_or_404()
    
    # محصولات مشابه 
    another_products = Product.query.filter(Product.active == 1).filter(Product.name.like(f'%{product.name[0:2]}%')).order_by(func.random()).limit(3).all()
    
    
    return render_template("product.html", product = product , another_products = another_products)


@app.route('/about')
def about():
    return render_template("about.html")