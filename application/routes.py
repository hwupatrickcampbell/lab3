from application import app
from flask import render_template, request
from flask import url_for,redirect
from application.forms import SignUpForm, SignInForm
from application.tables import db, Ticket

@app.route("/")
@app.route("/index")
@app.route("/hoho")
def index():
    return render_template("index.html", index=True, login=False)

@app.route("/products")
@app.route("/items")
def products():
    dataTicket = Ticket.query.filter_by(TYPE='Bug')
    return render_template("products.html", products=True, dataTicket=dataTicket)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    username = request.form.get("username", "")
    email = request.form.get("email", "")
    password = request.form.get("password", "")
    data = {"username": username, "email": email, "password": password}
    form = SignUpForm();
    return render_template("signup.html", signup = True, data = data, form=form)

@app.route("/basket")
def basket():
    return render_template("basket.html", basket = True, login = False)

@app.route("/signin", methods=["GET", "POST"])
def signin():
    TicketNumber = request.form.get("TicketNumber", "")
    if request.form:
        ticket = Ticket(TicketNumber=request.form.get("TicketNumber"))
        db.session.add(ticket)
        db.session.commit()
        return redirect(url_for("products"))
    username = request.form.get("username", "")
    TYPE = request.form.get("TYPE", "")
    StoryPoints = request.form.get("StoryPoints", "")
    data = {"TicketNumber": TicketNumber, "username": username, "TYPE": TYPE, "StoryPoints": StoryPoints}
    form = SignInForm();
    return render_template("signin.html", signin = True, data = data, form = form)
