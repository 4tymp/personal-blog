from flask import Flask,render_template, request
import json
import os

app = Flask(__name__)

# Folder, w którym będą przechowywane pliki artykułów
ARTICLE_FOLDER = "articles"

# Upewnij się, że folder istnieje
if not os.path.exists(ARTICLE_FOLDER):
    os.makedirs(ARTICLE_FOLDER)

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

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/add", methods =["GET","POST"])
def add():

    if request.method== "POST":
        title = request.form["title"]
        date = request.form["date"]
        content = request.form["content"]

        # Odczytanie plików artykułów w folderze
        article_list = []
        for filename in os.listdir(ARTICLE_FOLDER):
            if filename.endswith(".json"):
                article_path = os.path.join(ARTICLE_FOLDER, filename)
                with open(article_path, "r") as file:
                    article = json.load(file)
                    article_list.append(article)

        # Zwiększenie id na podstawie istniejących artykułów
        if article_list:
            new_id = max(article['id'] for article in article_list) + 1
        else:
            new_id = 1

        # Utworzenie nowego artykułu
        article = {
            "id": new_id,
            "title": title,
            "date": date,
            "content": content
        }

        # Zapisanie artykułu do osobnego pliku
        article_name = f"article{new_id}.json"
        article_path = os.path.join(ARTICLE_FOLDER, article_name)
        with open(article_path, "w") as f:
            f.write(json.dumps(article))

        return redirect(url_for('admin'))

    return render_template("add.html")