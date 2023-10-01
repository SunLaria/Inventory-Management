from flask import Flask,redirect,url_for,render_template,request
from sql import create_database,add_row,load,delete,search
create_database()

app=Flask(__name__)
@app.route('/')
def dashboard():
    return render_template('dashboard.html',products_data=load("products"),listings_data=load("listings"),purchases_data=load("purchases"))

@app.route("/products")
def products():
    return render_template('products.html',data=load("products"))

@app.route("/purchases")
def purchases():
    return render_template("purchases.html",data=load("purchases"))

@app.route("/listings")
def listings():
    return render_template("listings.html",data = load("listings"))

@app.route("/searchp/")
def search_purchase():
    return render_template("search.html",data = search("purchases",request.args["pid"]))