#importing modules
from flask import Flask , render_template

#creating a flask instance
app = Flask(__name__)

#create a route decorator
@app.route('/')

def index():
    return "<h1>Hello World!</h1>"
# this route will be specific and go to the users page
#localhost:5000/user/rio
@app.route('/user/<name>')
def user(name):
    return "<h1>Hello {}!!</h1>".format(name)