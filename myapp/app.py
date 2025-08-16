from flask import Flask,render_template

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("home.html")


@app.get("/about")
def about():
    return render_template("about.html")


@app.get("/contact")
def contact():
    contacts = contact.query.order_by(contact.name.asc()).all()
    return render_template("contact.html", contacts=contacts)


@app.get("/create_contact")
def create_contact():
    return render_template("create_contact.html")


@app.get("/edit_contact")
def create_contact():
    return render_template("edit_contact.html")
