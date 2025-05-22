from flask import Flask, render_template, redirect, request
from random import randint


#create the app
app = Flask(__name__) 

@app.get("/")
def home():
    return render_template('pages/home.jinja')

@app.get("/about/")
def about():
    return render_template('/pages/about.jinja')

@app.get("/random/")
def random_number():
    randNum = str(randint(1,1000))
    return render_template('/pages/random.jinja' , number=randNum)

@app.get("/number/<int:num>")
def analyseNumber(num):
    return render_template("pages/number.jinja",number=num)

@app.get("/form/")
def form():
    return render_template("/pages/form.jinja")

@app.errorhandler(404)
def notfound(e):
    return render_template("pages/404.jinja")