from flask import Flask, render_template, redirect, request, flash
from cs50 import SQL
from urllib.parse import quote


db = SQL("sqlite:///sensidb.db")



app = Flask(__name__)

app.secret_key = "welcometosensi"




@app.route("/", methods = ["GET", "POST"])
def index():

    return render_template("index.html")
  


@app.route("/developer", methods = ["GET", "POST"])
def developer():

    return render_template("developer.html")


@app.route("/about", methods = ["GET", "POST"])
def about():

    return render_template("about.html")

@app.route("/contact", methods = ["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message_body = request.form.get("message")

        if not name or not email or not message_body:
            flash("Please fill out all fields.", "danger")
            return redirect("/contact")

        recipient = "astkun010@gmail.com"
        subject = quote(f"Message from {name}")
        body = quote(f"Name: {name}\nEmail: {email}\n\n{message_body}")

        mailto_link = f"mailto:{recipient}?subject={subject}&body={body}"

        return redirect(mailto_link)
    
    return render_template("contact.html")



@app.route("/newsletter", methods=["POST"])
def newsletter():
    email = request.form.get("email-newsletter")
    if email:
        isexist = db.execute("SELECT * FROM newsletter WHERE email = ?", email)
        if not isexist:
            db.execute("INSERT INTO newsletter (email) VALUES (?)", email)
            flash("Subscribed successfully!", "success")
        else:
            flash("You’re already subscribed.", "info")
    return redirect(request.referrer or "/")
