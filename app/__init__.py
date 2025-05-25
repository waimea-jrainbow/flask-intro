from flask import Flask, render_template, redirect, request
from random import randint


#create the app
app = Flask(__name__) 


# Home page - loading a static page
@app.get("/")
def home():
    return render_template('pages/home.jinja')

#-----------------------------------------------
# About page - loading a static page
@app.get("/about/")
def about():
    return render_template('/pages/about.jinja')

#-----------------------------------------------
# Random number page - passing a value into the template
@app.get("/random/")
def random_number():
    randNum = str(randint(1,1000))
    return render_template('/pages/random.jinja' , number=randNum)

#-----------------------------------------------
# Number page - retrieving a value from route (url)
#               and passing into template 
@app.get("/number/<int:num>")
def analyseNumber(num):
    return render_template("pages/number.jinja",number=num)

#-----------------------------------------------
# Form page - Static page with a form
@app.get("/form/")
def form():
    return render_template("/pages/form.jinja")


#------------------------------------------------
# Handle data POSTed from the form
@app.post("/processForm")
def processForm():
    print(f"Form data: ${request.form}")
    return render_template(
        "pages/formData.jinja",
        name = request.form["name"],
        age = request.form["age"]
    )

#-----------------------------------------------
# Handle any missing pages
@app.errorhandler(404)
def notfound(e):
    return render_template("pages/404.jinja")