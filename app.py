from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login", methods =["GET","POST"])
def login():
    result = None

    if request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]

        if login == "admin" and password == "admin":
            result = True
        else:
            result = False

    return render_template("login.html", result=result)