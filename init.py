import os
import main, slack

from flask import Flask, render_template
from appdef import app, conn

# SECRET_KEY = os.environ['SECRET_KEY']

if __name__ == "__main__":
  # app.secret_key = SECRET_KEY
  app.run('localhost', 5000, debug = True)
