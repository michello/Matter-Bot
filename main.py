# homepage
# probably where we'll showcase the posts/exchanges that's been made
from flask import *
from appdef import app

@app.route('/')
def main():
  return render_template("index.html")
