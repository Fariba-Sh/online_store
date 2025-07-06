from flask import Blueprint, render_template, session , redirect , request , abort
import config


app = Blueprint("admin", __name__)


@app.before_request
def before_request():
       if session.get('admin_login' , None) == None and request.endpoint != "admin.login" :
        abort(403)
        # abort 403 :forbiden



@app.route('/admin' , methods = ["POST" , "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username", None)
        password = request.form.get("password" , None)
    
        if username == config.ADMIN_USERNAME and password == config.ADMIN_PASSWORD :
            session['admin_login'] = username
            return redirect("admin/dashboard")
        else:
            return redirect("admin")

    
    else:
        return render_template("admin/login.html")


@app.route('/admin/dashboard' , methods = ["GET"])
def dashboard_admin():
    return render_template("admin/dashboard.html")



@app.route('/admin/dashboard/products' , methods = ["GET"])
def products_admin():
    return render_template("admin/products.html")