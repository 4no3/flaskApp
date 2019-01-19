from flask import Flask
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename
from random import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hoge", message="Fuga")
    # return render_template("index.html", lst=[
    #     {"name": "Hoge", "value": "1"},
    #     {"name": "Fuga", "value": "2"}, 
    #     {"name": "Foo", "value": "3"}
    #     ])
    # return render_template("index.html", random=random())
    # return render_template("index.html", title="Hello World")
    # return render_template("index.html", obj={"title" : "hoge"})
    # return """
    #     <!DOCTYPE html>
    #     <html>
    #         <head>
    #             <meta charset="utf-8"/>
    #             <link rel="stylesheet" href="/static/style.css"/>
    #         </head>
    #         <body>
    #             <h1>Hello World</h1>
    #         </body>
    #     </html>
    # """


@app.route("/foo/")
def foo():
    return "foo"


@app.route("/fuga")
def fuga():
    return "fuga"


@app.route("/title/<title>")
def title(title):
    return render_template("index.html", title=title)


@app.route("/search")
def search():
    q = request.args.get("q", "")
    return q


@app.route("/login", methods=["GET"])
def render_form():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    if request.form["username"] and request.form["email"]:
        return render_template("check.html", email=request.form["email"], username=request.form["username"])
    else:
        return render_template("error.html")


@app.route("/upload", methods=["GET"])
def render_upload_form():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    if request.form["name"] and request.files["image"]:
        f = request.files["image"]
        filepath = "static/" + secure_filename(f.filename)
        f.save(filepath)
        return render_template("result.html", name=request.form["name"], image_url=filepath)

