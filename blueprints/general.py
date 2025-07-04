from flask import Blueprint

app = Blueprint("general", __name__)

@app.route('/')
def hello_world():
    return 'helloww world! this is the main page'