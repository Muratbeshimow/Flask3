from unittest import result
from flask import Flask, render_template, request
import datetime
app = Flask(__name__)


@app.route('/')
def login():
    return render_template("targilim.html")


@app.route('/targil1')
def targil1():
    return render_template("targil1.html", name=request.args["username"], date=datetime.datetime.today())


@app.route('/targil2')
def hello_response():
    if request.args["username"] == "tal":
        message = f"Hello, {request.args['username']}"
    else:
        message = "Unauthorized"
    return render_template("targil2.html", message=message)


@app.route('/targil3')
def targil3():
    return render_template("targil3.html", firstname=request.args["firstname"], lastname=request.args["lastname"])


@app.route('/targil4')
def targil4():
    price = request["price"]
    result = int(price)*1.17
    return render_template("targil4.html", result=str(result))
