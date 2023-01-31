#!/usr/bin/env python3
"""
app's module
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ The home page for the website
    """
    return render_template("index.html")
