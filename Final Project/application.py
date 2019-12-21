import os
import requests
import json


from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
# from googleplaces import GooglePlaces, types

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
db = SQL("sqlite:///weset.db")

# Make sure API key is set
# if not os.environ.get("API_KEY"):
#     raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    # """Show portfolio of stocks"""
    # return apology("TODO")
    #https://www.jquery-az.com/7-examples-explain-sql-select-distinct-mysql-sql-server/

    #get all necessary variables
    mydict = {}
    myid = session["user_id"]
    conc = db.execute("SELECT conc FROM myusers WHERE id = :myid", myid = session["user_id"])
    conc = conc[0]["conc"]
    class1 = db.execute("SELECT class1 FROM myusers WHERE id = :myid", myid = session["user_id"])
    class1 = class1[0]["class1"]
    class2 = db.execute("SELECT class2 FROM myusers WHERE id = :myid", myid = session["user_id"])
    class2 = class2[0]["class2"]
    class3 = db.execute("SELECT class3 FROM myusers WHERE id = :myid", myid = session["user_id"])
    class3 = class3[0]["class3"]
    class4 = db.execute("SELECT class4 FROM myusers WHERE id = :myid", myid = session["user_id"])
    class4 = class4[0]["class4"]
    class5 = db.execute("SELECT class5 FROM myusers WHERE id = :myid", myid = session["user_id"])
    class5 = class5[0]["class5"]
    class6 = db.execute("SELECT class6 FROM myusers WHERE id = :myid", myid = session["user_id"])
    class6 = class6[0]["class6"]
    online = db.execute("SELECT online FROM myusers WHERE id = :myid", myid = session["user_id"])
    online = online[0]["online"]
    morn = db.execute("SELECT morn FROM myusers WHERE id = :myid", myid = session["user_id"])
    morn = morn[0]["morn"]
    aft = db.execute("SELECT aft FROM myusers WHERE id = :myid", myid = session["user_id"])
    aft = aft[0]["aft"]
    eve = db.execute("SELECT eve FROM myusers WHERE id = :myid", myid = session["user_id"])
    eve = eve[0]["eve"]
    night = db.execute("SELECT night FROM myusers WHERE id = :myid", myid = session["user_id"])
    night = night[0]["night"]
    latenight = db.execute("SELECT latenight FROM myusers WHERE id = :myid", myid = session["user_id"])
    latenight = latenight[0]["latenight"]
    loc1 = db.execute("SELECT loc1 FROM myusers WHERE id = :myid", myid = session["user_id"])
    loc1 = loc1[0]["loc1"]
    loc2 = db.execute("SELECT loc2 FROM myusers WHERE id = :myid", myid = session["user_id"])
    loc2 = loc2[0]["loc2"]
    loc3 = db.execute("SELECT loc3 FROM myusers WHERE id = :myid", myid = session["user_id"])
    loc3 = loc3[0]["loc3"]
    house = db.execute("SELECT house FROM myusers WHERE id = :myid", myid = session["user_id"])
    house = house[0]["house"]

    #make a list for each class
    if class1:
        class1matches = db.execute("SELECT fname, lname, contactinfo FROM myusers WHERE conc = :conc AND (((morn = :morn AND morn = :mornvalue)) OR ((aft = :aft AND aft = :aftvalue)) OR ((eve = :eve AND eve = :evevalue)) OR ((night = :night AND night = :nightvalue)) OR ((latenight = :latenight AND latenight = :latenightvalue))) AND (class1 = :class1 OR class2 = :class1 OR class3 = :class1 OR class4 = :class1 OR class5 = :class1 OR class6 = :class1) AND ((online = :online AND online = :onlinevalue)) AND (id != :myid) GROUP BY lname", conc = conc, morn = morn, mornvalue = 1, aft = aft, aftvalue = 1, eve = eve, evevalue = 1, night = night, nightvalue = 1, latenight = latenight, latenightvalue = 1,class1 = class1, online = online, onlinevalue = 1, myid = myid)
        mydict[class1] = class1matches
    if class2:
        class2matches = db.execute("SELECT fname, lname, contactinfo FROM myusers WHERE conc = :conc AND (((morn = :morn AND morn = :mornvalue)) OR ((aft = :aft AND aft = :aftvalue)) OR ((eve = :eve AND eve = :evevalue)) OR ((night = :night AND night = :nightvalue)) OR ((latenight = :latenight AND latenight = :latenightvalue))) AND (class1 = :class2 OR class2 = :class2 OR class3 = :class2 OR class4 = :class2 OR class5 = :class2 OR class6 = :class2) AND ((online = :online AND online = :onlinevalue)) AND (id != :myid) GROUP BY lname", conc = conc, morn = morn, mornvalue = 1, aft = aft, aftvalue = 1, eve = eve, evevalue = 1, night = night, nightvalue = 1, latenight = latenight, latenightvalue = 1,class2 = class2, online = online, onlinevalue = 1, myid = myid)
        mydict[class2] = class2matches
    if class3:
        class3matches = db.execute("SELECT fname, lname, contactinfo FROM myusers WHERE conc = :conc AND (((morn = :morn AND morn = :mornvalue)) OR ((aft = :aft AND aft = :aftvalue)) OR ((eve = :eve AND eve = :evevalue)) OR ((night = :night AND night = :nightvalue)) OR ((latenight = :latenight AND latenight = :latenightvalue))) AND (class1 = :class3 OR class2 = :class3 OR class3 = :class3 OR class4 = :class3 OR class5 = :class3 OR class6 = :class3) AND ((online = :online AND online = :onlinevalue)) AND (id != :myid) GROUP BY lname", conc = conc, morn = morn, mornvalue = 1, aft = aft, aftvalue = 1, eve = eve, evevalue = 1, night = night, nightvalue = 1, latenight = latenight, latenightvalue = 1,class3 = class3, online = online, onlinevalue = 1, myid = myid)
        mydict[class3] = class3matches
    if class4:
        class4matches = db.execute("SELECT fname, lname, contactinfo FROM myusers WHERE conc = :conc AND (((morn = :morn AND morn = :mornvalue)) OR ((aft = :aft AND aft = :aftvalue)) OR ((eve = :eve AND eve = :evevalue)) OR ((night = :night AND night = :nightvalue)) OR ((latenight = :latenight AND latenight = :latenightvalue))) AND (class1 = :class4 OR class2 = :class4 OR class3 = :class4 OR class4 = :class4 OR class5 = :class4 OR class6 = :class4) AND ((online = :online AND online = :onlinevalue)) AND (id != :myid) GROUP BY lname", conc = conc, morn = morn, mornvalue = 1, aft = aft, aftvalue = 1, eve = eve, evevalue = 1, night = night, nightvalue = 1, latenight = latenight, latenightvalue = 1,class4 = class4, online = online, onlinevalue = 1, myid = myid)
        mydict[class4] = class4matches
    if class5:
        class5matches = db.execute("SELECT fname, lname, contactinfo FROM myusers WHERE conc = :conc AND (((morn = :morn AND morn = :mornvalue)) OR ((aft = :aft AND aft = :aftvalue)) OR ((eve = :eve AND eve = :evevalue)) OR ((night = :night AND night = :nightvalue)) OR ((latenight = :latenight AND latenight = :latenightvalue))) AND (class1 = :class5 OR class2 = :class5 OR class3 = :class5 OR class4 = :class5 OR class5 = :class5 OR class6 = :class5) AND ((online = :online AND online = :onlinevalue)) AND (id != :myid) GROUP BY lname", conc = conc, morn = morn, mornvalue = 1, aft = aft, aftvalue = 1, eve = eve, evevalue = 1, night = night, nightvalue = 1, latenight = latenight, latenightvalue = 1,class5 = class5, online = online, onlinevalue = 1, myid = myid)
        mydict[class5] = class5matches
    if class6:
        class6matches = db.execute("SELECT fname, lname, contactinfo FROM myusers WHERE conc = :conc AND (((morn = :morn AND morn = :mornvalue)) OR ((aft = :aft AND aft = :aftvalue)) OR ((eve = :eve AND eve = :evevalue)) OR ((night = :night AND night = :nightvalue)) OR ((latenight = :latenight AND latenight = :latenightvalue))) AND (class1 = :class6 OR class2 = :class6 OR class3 = :class6 OR class4 = :class6 OR class5 = :class6 OR class6 = :class6) AND ((online = :online AND online = :onlinevalue)) AND (id != :myid) GROUP BY lname", conc = conc, morn = morn, mornvalue = 1, aft = aft, aftvalue = 1, eve = eve, evevalue = 1, night = night, nightvalue = 1, latenight = latenight, latenightvalue = 1,class6 = class6, online = online, onlinevalue = 1, myid = myid)
        mydict[class6] = class6matches

    #random, non-class-specific partners
    onlinematches = db.execute("SELECT fname, lname, contactinfo, loc1, loc2, loc3, house FROM myusers WHERE (((morn = :morn AND morn = :mornvalue)) OR ((aft = :aft AND aft = :aftvalue)) OR ((eve = :eve AND eve = :evevalue)) OR ((night = :night AND night = :nightvalue)) OR ((latenight = :latenight AND latenight = :latenightvalue))) AND (loc1 = :loc1 OR loc1 = :loc2 OR loc1 = :loc3 OR loc2 = :loc1 OR loc2 = :loc2 OR loc2 = :loc3 OR loc3 = :loc1 OR loc3 = :loc2 OR loc3 = :loc3 OR house = :house) AND ((online = :online AND online = :onlinevalue)) AND (id != :myid) GROUP BY lname", morn = morn, mornvalue = 1, aft = aft, aftvalue = 1, eve = eve, evevalue = 1, night = night, nightvalue = 1, latenight = latenight, latenightvalue = 1, loc1 = loc1, loc2 = loc2, loc3 = loc3, house = house, online = online, onlinevalue = 1, myid = myid)

    #if empty, need more info!
    if not mydict:
        return render_template("blankindex.html")
    #not too necessary anymore, keeping if needed for another edit
    if loc1 == "house1" or loc1 == "house2" or loc1 == "house3":
        loc1 = "House Library"
    if loc2 == "house1" or loc2 == "house2" or loc2 == "house3":
        loc2 = "House Library"
    if loc3 == "house1" or loc3 == "house2" or loc3 == "house3":
        loc3 = "House Library"
    if loc1 == "widener1" or loc1 == "widener2" or loc1 == "widener3":
        loc1 = "Widener Library"
    if loc2 == "widener1" or loc2 == "widener2" or loc2 == "widener3":
        loc2 = "Widener Library"
    if loc3 == "widener1" or loc3 == "widener2" or loc3 == "widener3":
        loc3 = "Widener Library"
    if loc1 == "widener1" or loc1 == "widener2" or loc1 == "widener3":
        loc1 = "Widener Library"
    if loc2 == "widener1" or loc2 == "widener2" or loc2 == "widener3":
        loc2 = "Widener Library"
    if loc3 == "widener1" or loc3 == "widener2" or loc3 == "widener3":
        loc3 = "Widener Library"
    if loc1 == "barker1" or loc1 == "barker2" or loc1 == "barker3":
        loc1 = "Barker Center"
    if loc2 == "barker1" or loc2 == "barker2" or loc2 == "barker3":
        loc2 = "Barker Center"
    if loc3 == "barker1" or loc3 == "barker2" or loc3 == "barker3":
        loc3 = "Barker Center"
    if loc1 == "md1" or loc1 == "md2" or loc1 == "md3":
        loc1 = "Maxwell Dworkin"
    if loc2 == "md1" or loc2 == "md2" or loc2 == "md3":
        loc2 = "Maxwell Dworkin"
    if loc3 == "md1" or loc3 == "md2" or loc3 == "md3":
        loc3 = "Maxwell Dworkin"
    if loc1 == "other1" or loc1 == "other2" or loc1 == "other3":
        loc1 = "Other"
    if loc2 == "other1" or loc2 == "other2" or loc2 == "other3":
        loc2 = "Other"
    if loc3 == "other1" or loc3 == "other2" or loc3 == "other3":
        loc3 = "Other"
    house = house.capitalize()
    # newname = mydict.get('a')[0]["fname"]
    # return apology(newname, 401)
    # namevicky = matches[0]["fname"]
    # return apology(namevicky, 401)
    # newdict = {'a':'a', 'b':'b', 'c':'c'}

    return render_template("index.html", matches = mydict, onlinematches = onlinematches, loc1 = loc1, loc2 = loc2, loc3 = loc3, house = house)


@app.route("/register", methods=["GET", "POST"])
def register():
    # """Register user"""
    # return apology("TODO")
    #referenced https://stackoverflow.com/questions/35005624/flask-login-login-user-and-redirect-to-home-page-after-registration
    # Forget any user_id
    #https://www.geeksforgeeks.org/python-program-check-string-contains-special-character/
    #https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

    #similar concept as finance pset
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
        # return apology(hash, 401)
        db.execute("INSERT INTO myusers (username, hash) VALUES (:username, :hash)", username = username, hash = hash)
        # return redirect(url_for("login"))
        return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    #similar concept as finance pset
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
        rows = db.execute("SELECT * FROM myusers WHERE username = :username",
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

@app.route("/pref", methods=["GET", "POST"])
@login_required
def pref():

    #referenced https://stackoverflow.com/questions/5904969/how-to-print-a-dictionarys-key
    if request.method == "GET":
        #rememberance!!
        myfname = db.execute("SELECT fname FROM myusers WHERE id = :myid", myid = session["user_id"])
        fname = myfname[0]["fname"]
        #if null, set to empty string so placeholder can show
        if fname is None:
            fname = ""
        mylname = db.execute("SELECT lname FROM myusers WHERE id = :myid", myid = session["user_id"])
        lname = mylname[0]["lname"]
        if lname is None:
            lname = ""
        # if lname == "":
        #     lname = "Last Name"
        year = db.execute("SELECT year FROM myusers WHERE id = :myid", myid = session["user_id"])
        year = str(year[0]["year"])
        # return apology(year, 403)

        #select boxes are harder, so this short demo will apply to the rest. Here goes.
        #make a dict with values
        thisdict = {'first_year':"first_year", 'sophomore':"sophomore", 'junior':"junior", 'senior': "senior"}
        #loop through them and if it equals the entry for current user, mark as selected. otherwise empty string so it doesn't affect selection
        for k, v in thisdict.items():
            if  v == year:
                thisdict[k] = "selected"
            else:
                thisdict[k] = ""
        #assign selection or empty string to variables, to be passed in to sql database later
        first_year = thisdict['first_year']
        sophomore = thisdict['sophomore']
        junior = thisdict['junior']
        senior = thisdict['senior']
        conc = db.execute("SELECT conc FROM myusers WHERE id = :myid", myid = session["user_id"])
        conc = conc[0]["conc"]
        thisdict = {'aaas':"aaas", 'anthro':"anthro", 'am':"am", 'afvs': "afvs", 'astro': "astro", 'beng': "beng", 'chemphysbio': "chemphysbio", 'chem': "chem",'chemphys': "chemphys", 'classics': "classics", 'complit': "complit", 'cs': "cs", 'eps': "eps", 'eas': "eas", 'econ': "econ", 'ee': "ee", 'es': "es", 'eng': "eng", 'ese': "ese", 'espp': "espp", 'folk': "folk", 'german': "german", 'gov': "gov", 'hist': "hist", 'histlit': "histlit", 'histsci': "histsci", 'histart': "histart", 'hdrb': "hdrb", 'heb': "heb", 'ib': "ib", 'ling': "ling", 'math': "math", 'me': "me", 'mcb': "mcb", 'music': "music", 'neareast': "neareast", 'neuro': "neuro", 'phil': "phil", 'physics': "physics", 'psych': "psych", 'religion': "religion", 'romance': "romance", 'slavic': "slavic", 'ss': "ss", 'socio': "socio",'sas': "sas", 'special': "special", 'stat': "stat", 'tdm': "tdm", 'wgs': "wgs"}
        for k, v in thisdict.items():
            if  v == conc:
                thisdict[k] = "selected"
            else:
                thisdict[k] = ""
        aaas = thisdict['aaas']
        anthro = thisdict['anthro']
        am = thisdict['am']
        afvs = thisdict['afvs']
        astro = thisdict['astro']
        beng = thisdict['beng']
        chemphysbio = thisdict['chemphysbio']
        chem = thisdict['chem']
        chemphys = thisdict['chemphys']
        classics = thisdict['classics']
        complit = thisdict['complit']
        cs = thisdict['cs']
        eps = thisdict['eps']
        eas = thisdict['eas']
        econ = thisdict['econ']
        ee = thisdict['ee']
        es = thisdict['es']
        eng = thisdict['eng']
        ese = thisdict['ese']
        espp = thisdict['espp']
        folk = thisdict['folk']
        german = thisdict['german']
        gov = thisdict['gov']
        hist = thisdict['hist']
        histlit = thisdict['histlit']
        histsci = thisdict['histsci']
        histart = thisdict['histart']
        hdrb = thisdict['hdrb']
        heb = thisdict['heb']
        ib = thisdict['ib']
        ling = thisdict['ling']
        math = thisdict['math']
        me = thisdict['me']
        mcb = thisdict['mcb']
        music = thisdict['music']
        neareast = thisdict['neareast']
        neuro = thisdict['neuro']
        phil = thisdict['phil']
        physics = thisdict['physics']
        psych = thisdict['psych']
        religion = thisdict['religion']
        romance = thisdict['romance']
        slavic = thisdict['slavic']
        ss = thisdict['ss']
        socio = thisdict['socio']
        sas = thisdict['sas']
        special = thisdict['special']
        stat = thisdict['stat']
        tdm = thisdict['tdm']
        wgs = thisdict['wgs']
        house = db.execute("SELECT house FROM myusers WHERE id = :myid", myid = session["user_id"])
        house = house[0]["house"]
        thisdict = {'adams':"adams", 'cabot':"cabot", 'currier':"currier", 'dunster': "dunster", 'dudley': "dudley", 'eliot': "eliot", 'kirkland': "kirkland", 'leverett': "leverett",'lowell': "lowell", 'mather': "mather", 'pfoho': "pfoho", 'quincy': "quincy", 'winthrop': "winthrop", 'apley': "apley", 'canaday': "canaday", 'dew': "dew", 'grays': "grays", 'green': "green", 'hollis': "hollis", 'holworthy': "holworthy", 'hurlbut': "hurlbut", 'lionel': "lionel", 'massachusetts': "massachusetts", 'matthews': "matthews", 'mower': "mower", 'pennypacker': "pennypacker", 'stoughton': "stoughton", 'straus': "straus", 'thayer': "thayer", 'weld': "weld", 'wigg': "wigg"}
        for k, v in thisdict.items():
            if  v == house:
                thisdict[k] = "selected"
            else:
                thisdict[k] = ""
        adams = thisdict['adams']
        cabot = thisdict['cabot']
        currier = thisdict['currier']
        dunster = thisdict['dunster']
        dudley = thisdict['dudley']
        eliot = thisdict['eliot']
        kirkland = thisdict['kirkland']
        leverett = thisdict['leverett']
        lowell = thisdict['lowell']
        mather = thisdict['mather']
        pfoho = thisdict['pfoho']
        quincy = thisdict['quincy']
        winthrop = thisdict['winthrop']
        apley = thisdict['apley']
        canaday = thisdict['canaday']
        dew = thisdict['dew']
        grays = thisdict['grays']
        green = thisdict['green']
        hollis = thisdict['hollis']
        holworthy = thisdict['holworthy']
        hurlbut = thisdict['hurlbut']
        lionel = thisdict['lionel']
        massachusetts = thisdict['massachusetts']
        matthews = thisdict['matthews']
        mower = thisdict['mower']
        pennypacker = thisdict['pennypacker']
        stoughton = thisdict['stoughton']
        straus = thisdict['straus']
        thayer = thisdict['thayer']
        weld = thisdict['weld']
        wigg = thisdict['wigg']
        contactmethod = db.execute("SELECT contactmethod FROM myusers WHERE id = :myid", myid = session["user_id"])
        contactmethod = str(contactmethod[0]["contactmethod"])
        thisdict = {'email':"email", 'phone':"phone", 'fb':"fb", 'other': "other"}
        for k, v in thisdict.items():
            if  v == contactmethod:
                thisdict[k] = "selected"
            else:
                thisdict[k] = ""
        email = thisdict['email']
        phone = thisdict['phone']
        fb = thisdict['fb']
        other = thisdict['other']
        contactinfo = db.execute("SELECT contactinfo FROM myusers WHERE id = :myid", myid = session["user_id"])
        contactinfo = contactinfo[0]["contactinfo"]
        if contactinfo is None:
            contactinfo = ""
        class1 = db.execute("SELECT class1 FROM myusers WHERE id = :myid", myid = session["user_id"])
        class1 = class1[0]["class1"]
        if class1 is None:
            class1 = ""
        class2 = db.execute("SELECT class2 FROM myusers WHERE id = :myid", myid = session["user_id"])
        class2 = class2[0]["class2"]
        if class2 is None:
            class2 = ""
        class3 = db.execute("SELECT class3 FROM myusers WHERE id = :myid", myid = session["user_id"])
        class3 = class3[0]["class3"]
        if class3 is None:
            class3 = ""
        class4 = db.execute("SELECT class4 FROM myusers WHERE id = :myid", myid = session["user_id"])
        class4 = class4[0]["class4"]
        if class4 is None:
            class4 = ""
        class5 = db.execute("SELECT class5 FROM myusers WHERE id = :myid", myid = session["user_id"])
        class5 = class5[0]["class5"]
        if class5 is None:
            class5 = ""
        class6 = db.execute("SELECT class6 FROM myusers WHERE id = :myid", myid = session["user_id"])
        class6 = class6[0]["class6"]
        if class6 is None:
            class6 = ""
        loc1 = db.execute("SELECT loc1 FROM myusers WHERE id = :myid", myid = session["user_id"])
        loc1 = loc1[0]["loc1"]
        thisdict = {'house1':"house1", 'widener1':"widener1", 'barker1':"barker1", 'md1': "md1", 'other1': "other1"}
        for k, v in thisdict.items():
            if  v == loc1:
                thisdict[k] = "selected"
            else:
                thisdict[k] = ""
        house1 = thisdict['house1']
        widener1 = thisdict['widener1']
        barker1 = thisdict['barker1']
        md1 = thisdict['md1']
        other1 = thisdict['other1']
        loc2 = db.execute("SELECT loc2 FROM myusers WHERE id = :myid", myid = session["user_id"])
        loc2 = loc2[0]["loc2"]
        thisdict = {'house2':"house2", 'widener2':"widener2", 'barker2':"barker2", 'md2': "md2", 'other2': "other2"}
        for k, v in thisdict.items():
            if  v == loc2:
                thisdict[k] = "selected"
            else:
                thisdict[k] = ""
        house2 = thisdict['house2']
        widener2 = thisdict['widener2']
        barker2 = thisdict['barker2']
        md2 = thisdict['md2']
        other2 = thisdict['other2']
        loc3 = db.execute("SELECT loc3 FROM myusers WHERE id = :myid", myid = session["user_id"])
        loc3 = loc3[0]["loc3"]
        thisdict = {'house3':"house3", 'widener3':"widener3", 'barker3':"barker3", 'md3': "md3", 'other3': "other3"}
        for k, v in thisdict.items():
            if  v == loc2:
                thisdict[k] = "selected"
            else:
                thisdict[k] = ""
        house3 = thisdict['house3']
        widener3 = thisdict['widener3']
        barker3 = thisdict['barker3']
        md3 = thisdict['md3']
        other3 = thisdict['other3']
        online = db.execute("SELECT online FROM myusers WHERE id = :myid", myid = session["user_id"])
        online = online[0]["online"]
        if online == 1:
            online="checked"
        else:
            online=""
        morn = db.execute("SELECT morn FROM myusers WHERE id = :myid", myid = session["user_id"])
        morn = morn[0]["morn"]
        if morn == 1:
            morn="checked"
        else:
            morn=""
        aft = db.execute("SELECT aft FROM myusers WHERE id = :myid", myid = session["user_id"])
        aft = aft[0]["aft"]
        if aft == 1:
            aft="checked"
        else:
            aft=""
        eve = db.execute("SELECT eve FROM myusers WHERE id = :myid", myid = session["user_id"])
        eve = eve[0]["eve"]
        if eve == 1:
            eve="checked"
        else:
            eve=""
        night = db.execute("SELECT night FROM myusers WHERE id = :myid", myid = session["user_id"])
        night = night[0]["night"]
        if night == 1:
            night="checked"
        else:
            night=""
        latenight = db.execute("SELECT latenight FROM myusers WHERE id = :myid", myid = session["user_id"])
        latenight = latenight[0]["latenight"]
        if latenight == 1:
            latenight="checked"
        else:
            latenight=""
        # myfname = db.execute("SELECT fname FROM myusers WHERE id = :myid", myid = session["user_id"])
        # fname = myfname[0]["fname"]
        # myfname = db.execute("SELECT fname FROM myusers WHERE id = :myid", myid = session["user_id"])
        # fname = myfname[0]["fname"]
        # myfname = db.execute("SELECT fname FROM myusers WHERE id = :myid", myid = session["user_id"])
        # fname = myfname[0]["fname"]
        # myfname = db.execute("SELECT fname FROM myusers WHERE id = :myid", myid = session["user_id"])
        # fname = myfname[0]["fname"]
        # myfname = db.execute("SELECT fname FROM myusers WHERE id = :myid", myid = session["user_id"])
        # fname = myfname[0]["fname"]
        # myfname = db.execute("SELECT fname FROM myusers WHERE id = :myid", myid = session["user_id"])
        # fname = myfname[0]["fname"]
        # myfname = db.execute("SELECT fname FROM myusers WHERE id = :myid", myid = session["user_id"])
        # fname = myfname[0]["fname"]
        # myfname = db.execute("SELECT fname FROM myusers WHERE id = :myid", myid = session["user_id"])
        # fname = myfname[0]["fname"]
        # myfname = db.execute("SELECT fname FROM myusers WHERE id = :myid", myid = session["user_id"])
        # fname = myfname[0]["fname"]
        return render_template("preferences.html", morn=morn, aft=aft, eve=eve, night=night, latenight=latenight, fname = fname, lname = lname, first_year = first_year, sophomore = sophomore, junior = junior, senior = senior, aaas = aaas, anthro=anthro, am=am, afvs= afvs, astro= astro, beng= beng, chemphysbio= chemphysbio, chem= chem,chemphys= chemphys, classics=classics, complit= complit, cs= cs, eps= eps, eas= eas, econ= econ, ee= ee, es= es, eng= eng, ese= ese, espp= espp, folk= folk, german= german, gov= gov, hist= hist, histlit= histlit, histsci= histsci, histart= histart, hdrb= hdrb, heb= heb, ib= ib, ling= ling, math=math, me=me, mcb= mcb, music=music, neareast= neareast, neuro= neuro, phil= phil, physics= physics, psych= psych, religion=religion, romance=romance, slavic=slavic, ss=ss, socio=socio,sas=sas, special=special, stat=stat, tdm=tdm, wgs=wgs, adams=adams, cabot=cabot, currier=currier, dunster=dunster, dudley=dudley, eliot=eliot, kirkland=kirkland, leverett=leverett,lowell=lowell, mather=mather, pfoho=pfoho, quincy=quincy, winthrop=winthrop, apley=apley, canaday=canaday, dew=dew, grays=grays, green=green, hollis=hollis, holworthy=holworthy, hurlbut=hurlbut, lionel=lionel, massachusetts=massachusetts, matthews=matthews, mower=mower, pennypacker=pennypacker, stoughton=stoughton, straus=straus, thayer=thayer, weld=weld, wigg=wigg,email=email, phone=phone, fb=fb, other=other, contactinfo=contactinfo, class1=class1, class2=class2, class3=class3, class4=class4, class5=class5, class6=class6, house1=house1, widener1=widener1, barker1=barker1, md1=md1,other1=other1, house2=house2, widener2=widener2, barker2=barker2, md2=md2,other2=other2, house3=house3, widener3=widener3, barker3=barker3, md3=md3,other3=other3, online=online)
    else:
        #pull values from forms/boxes
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        year = request.form.get("year")
        conc = request.form.get("conc")
        house = request.form.get("house")
        contactmethod = request.form.get("contactmethod")
        contactinfo= request.form.get("contactinfo")
        class1= request.form.get("class1")
        class2= request.form.get("class2")
        class3= request.form.get("class3")
        class4= request.form.get("class4")
        class5= request.form.get("class5")
        class6= request.form.get("class6")
        loc1= request.form.get("loc1")
        loc2= request.form.get("loc2")
        loc3= request.form.get("loc3")
        morn = request.form.get("morn")
        aft = request.form.get("aft")
        eve = request.form.get("eve")
        night = request.form.get("night")
        latenight = request.form.get("latenight")
        online = request.form.get("online")
        #change selections to booleans
        if not morn:
            morn = 0
        else:
            morn=1
        if not aft:
            aft=0
        else:
            aft=1
        if not eve:
            eve=0
        else:
            eve=1
        if not night:
            night=0
        else:
            night=1
        if not latenight:
            latenight=0
        else:
            latenight=1
        if not online:
            online=0
        else:
            online=1
        #location info, never finished
        mylong = None
        mylat = None
        # response_data = requests.get('https://www.iplocation.net/go/ipinfo').text
        # try:
        #     response_json_data = json.loads(response_data)
        #     location = response_json_data["loc"].split(",")
        #     mylat = location[0]
        #     mylong = location[1]
        # except ValueError:
        #     return apology("ValueError", 403)


        #update entry for logged in user
        db.execute("UPDATE myusers SET fname = :fname, lname = :lname,year = :year, conc = :conc, house = :house, contactmethod = :contactmethod, contactinfo = :contactinfo, class1 = :class1, class2 = :class2, class3 = :class3, class4 = :class4, class5 = :class5, class6 = :class6, loc1 = :loc1, loc2 = :loc2, loc3 = :loc3,morn = :morn, aft = :aft, eve = :eve, night = :night, latenight = :latenight,online = :online WHERE id = :myid", fname = fname, lname = lname, year = year, conc = conc, house = house, contactmethod = contactmethod, contactinfo = contactinfo, class1 = class1, class2 = class2, class3 = class3, class4 = class4, class5 = class5, class6 = class6, loc1 = loc1, loc2 = loc2, loc3 = loc3, morn = morn, aft = aft, eve = eve, night = night, latenight = latenight, online = online, myid = session["user_id"])

        # db.execute("UPDATE myusers SET fname = :fname, lname = :lname, year = :year, conc = :conc, house = :house, contactmethod = :contactmethod, contactinfo = :contactinfo, class1 = :class1, class2 = :class2, class3 = :class3, class4 = :class4, class5 = :class5, class6 = :class6, loc1 = :loc1, loc2 = :loc2, loc3 = :loc3, morn = :morn, aft = :aft, eve = :eve, night = :night, latenight = :latenight, online = :online, mylong = :mylong, mylat = :mylat  WHERE id = :myid", fname = fname, lname = lname, year = year, conc = conc, house = house, contactmethod = contactmethod, contactinfo = contactinfo, class1 = class1, class2 = class2, class3 = class3, class4 = class4, class5 = class5, class6 = class6, loc1 = loc1, loc2 = loc2, loc3 = loc3, morn = morn, aft = aft, eve = eve, night = night, latenight = latenight, online = online, mylong = mylong, mylat = mylat, myid = session["user_id"])
        return redirect("/")

 #same idea as finance pset for the rest of these paths
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)



