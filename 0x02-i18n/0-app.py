#!/usr/bin/env python3
"""
app's module
"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """ The home page for the website
    """
    return render_template("index.html")


if __name__ == "__main__":
    """Run the app
    """
    app.run(host="0.0.0.0", port=5000)
