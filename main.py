from distutils.log import debug
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# import declared routes
import routes

app.run(debug=True)