from flask import Flask, render_template, request, url_for
import database

app = Flask(__name__)


@app.route('/', methods=['GET'])
def test():
    data = database.enter()
    return render_template("home.html",data = data)


