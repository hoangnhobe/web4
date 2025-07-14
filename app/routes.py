from flask import Blueprint, render_template, request, redirect, session
from app.models import get_db_connection

app_routes = Blueprint('app_routes', __name__)

@app_routes.route("/")
def home():
    return render_template("home.html")

@app_routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if user:
            session["user"] = username
            return redirect("/products")
    return render_template("login.html")

@app_routes.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users(username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect("/login")
    return render_template("register.html")

@app_routes.route("/products")
def products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("products.html", products=products)

@app_routes.route("/order/<int:product_id>")
def order(product_id):
    if "user" not in session:
        return redirect("/login")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders(username, product_id) VALUES (%s, %s)", (session["user"], product_id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("/myorders")

@app_routes.route("/myorders")
def myorders():
    if "user" not in session:
        return redirect("/login")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT o.id, p.name FROM orders o JOIN products p ON o.product_id = p.id WHERE o.username=%s", (session["user"],))
    orders = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("orders.html", orders=orders)

@app_routes.route("/cancel/<int:order_id>")
def cancel(order_id):
    if "user" not in session:
        return redirect("/login")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM orders WHERE id=%s AND username=%s", (order_id, session["user"]))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("/myorders")