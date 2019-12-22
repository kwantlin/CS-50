import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# def hasNumbers(inputString):
            # return bool(re.search(r'\d', inputString))

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    # """Show portfolio of stocks"""
    # return apology("TODO")
    #https://www.jquery-az.com/7-examples-explain-sql-select-distinct-mysql-sql-server/
    myid = session["user_id"]
    history = db.execute("SELECT symbol, names, SUM(shares), price, SUM(total), time FROM history WHERE names IN (SELECT DISTINCT(names) FROM history WHERE user_id = :myid) AND user_id = :myid GROUP BY names", myid = myid)
    return render_template("index.html", history = history)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    # """Buy shares of stock"""
    # return apology("TODO")
    #referenced https://stackoverflow.com/questions/4541155/check-if-a-number-is-int-or-float
    #https://stackoverflow.com/questions/5424716/how-to-check-if-string-input-is-a-number
    #https://www.btelligent.com/en/blog/best-practice-for-sql-statements-in-python/
    #https://www.w3schools.com/html/html_tables.asp
    if request.method == "GET":
            return render_template("buy.html")
    else:
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if lookup(symbol) == None:
            return apology("invalid symbol", 403)
        # if ((float(shares)).is_integer() == False and not shares.isdigit()):
        if not shares.isdigit():
            return apology("must purchase positive integer shares", 403)
        if int(shares) == 0:
            return apology("must purchase positive integer shares", 403)
        name = lookup(symbol)["name"]
        intshares = int(shares)
        currentpx = lookup(symbol)["price"]

        # currentid = str(session['user_id'])
        # return apology(currentid, 403)
        currentcashrow = db.execute("SELECT cash FROM users WHERE id = :myid", myid = session["user_id"])
        # return apology("here yet2", 403)
        currentcash = currentcashrow[0]["cash"]
        # return apology(currentcash, 403)
        amount = str(intshares*currentpx)
        # return apology(amount, 403)
        if (intshares*currentpx>currentcash):
            return apology("insufficient funds", 401)

        remaining = currentcash - intshares*currentpx
        db.execute("INSERT INTO history (user_id, symbol, names, shares, price, total) VALUES (:user_id, :symbol, :name, :shares, :price, :total)", user_id = session["user_id"], symbol = symbol, name = name, shares = intshares, price = currentpx, total = amount)
        # return apology("here yet1", 403)
        db.execute("UPDATE users SET cash = :cash WHERE id = :myid", cash = remaining, myid = session["user_id"])

        return redirect("/")
        # return render_template("quoted.html", name = "MINE", symbol = "MY", dollars = 100)


@app.route("/history")
@login_required
def history():
    # """Show history of transactions"""
    # return apology("TODO")
    myid = session["user_id"]
    history = db.execute("SELECT * FROM history WHERE user_id IS :myid", myid = myid)
    return render_template("history.html", history = history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    # """Get stock quote."""
    # return apology("TODO")
    #referenced https://stackoverflow.com/questions/5904969/how-to-print-a-dictionarys-key
    if request.method == "GET":
            return render_template("quote.html")
    else:
        symbol = request.form.get("symbol")
        if lookup(symbol) == None:
            return apology("invalid symbol", 400)
        else:
            # px = lookup(symbol)["price"]
            # priceminus = px[1:]
            # return render_template("quoted.html", name = lookup(symbol)["name"], symbol = lookup(symbol)["symbol"], dollars = px)
            return render_template("quoted.html", name = lookup(symbol)["name"], symbol = lookup(symbol)["symbol"], dollars = lookup(symbol)["price"])
            # return render_template("quoted.html", name = "MINE", symbol = "MY", dollars = 100)


@app.route("/register", methods=["GET", "POST"])
def register():
    # """Register user"""
    # return apology("TODO")
    #referenced https://stackoverflow.com/questions/35005624/flask-login-login-user-and-redirect-to-home-page-after-registration
    # Forget any user_id
    #https://www.geeksforgeeks.org/python-program-check-string-contains-special-character/
    #https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
    session.clear()

    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        if not username:
            return apology("must provide username", 401)
        password = request.form.get("password1")
        password2 = request.form.get("password2")
        if password != password2:
            return apology("passwords must match", 400)
        if not password:
            return apology("must provide password", 401)
        # if password.isUpper()==True or password.isLower()==True or hasNumbers(password) == False or len(password<8):
        #     return apology("Password must contain upper & lower case and at least one special char and one number, and be at least 8 characters", 401)
        hash = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username = username, hash = hash)
        # return redirect(url_for("login"))
        return redirect("/login")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    # """Sell shares of stock"""
    # return apology("TODO")
    if request.method == "GET":
            return render_template("sell.html")
    else:
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        name = lookup(symbol)["name"]
        if lookup(symbol) == None:
            return apology("invalid symbol", 403)
        # if ((float(shares)).is_integer() == False and not shares.isdigit()):
        if not shares.isdigit():
            return apology("must purchase positive integer shares", 403)
        if int(shares) == 0:
            return apology("must purchase positive integer shares", 403)

        myrow = db.execute("SELECT SUM(shares) FROM history WHERE names IS :name AND user_id = :myid", name = name, myid = session["user_id"])
        sharesowned = myrow[0]["SUM(shares)"]
        intshares = int(shares)

        if intshares > sharesowned:
            return apology("insufficient shares", 403)


        name = lookup(symbol)["name"]
        intshares = int(shares)*(-1)
        currentpx = lookup(symbol)["price"]
        # currentid = str(session['user_id'])

        currentcashrow = db.execute("SELECT cash FROM users WHERE id = :myid", myid = session["user_id"])
        # return apology("here yet2", 403)
        currentcash = currentcashrow[0]["cash"]
        # return apology(currentcash, 403)
        amount = str(intshares*currentpx)
        # return apology(amount, 403)
        remaining = currentcash - (intshares*currentpx)
        db.execute("INSERT INTO history (user_id, symbol, names, shares, price, total) VALUES (:user_id, :symbol, :name, :shares, :price, :total)", user_id = session["user_id"], symbol = symbol, name = name, shares = intshares, price = currentpx, total = amount)
        # return apology("here yet1", 403)
        db.execute("UPDATE users SET cash = :cash WHERE id = :myid", cash = remaining, myid = session["user_id"])

        return redirect("/")

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
