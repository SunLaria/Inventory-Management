from flask import Flask,redirect,url_for,render_template,request
from sql import create_database,add_row,load,delete,search,update_quantity
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

@app.route("/add-product" ,methods=["GET","POST"])
def add_product():
    if request.method=="GET":
        return render_template("add-product.html")
    if request.method=="POST":
        latest_id = int(load("products")[-1]["id"])+1
        product_info= {"id":latest_id,"name":request.form["name"],"quantity":request.form["quantity"],"category":request.form["category"],"avaiabillty":"none","price":request.form["price"]}
        add_row("products",product_info)
        return redirect("products")


@app.route("/update-quantity" ,methods=["GET","POST"])
def update_quantitys():
    if request.method=="GET" and len(request.args)>0:
        return render_template("update-quantity.html",product=search("products",request.args["id"])[0])
    if request.method=="POST":
        update_quantity(table_name = "products",id = request.form["id"],quantity = request.form["quantity"])
        return redirect("products")
    

@app.route("/delete_product" ,methods=["GET","POST"])
def delete_product():
    if request.method=="GET":
        return render_template("delete-product.html",product=search("products",request.args["id"])[0])
    if request.method=="POST":
        pass