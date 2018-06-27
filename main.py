from flask import *
from appdef import app

@app.route('/')
def main():
  return render_template("index.html")
