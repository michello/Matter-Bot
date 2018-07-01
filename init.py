import os
import main, slack

from flask import Flask, render_template
<<<<<<< HEAD
from appdef import app#, db
## each page will have its own python file/module, which will be imported from here:
import main, slack, google_sheets
=======
from appdef import app, conn

# SECRET_KEY = os.environ['SECRET_KEY']
>>>>>>> refs/remotes/origin/master

if __name__ == "__main__":
  # app.secret_key = SECRET_KEY
  app.run('localhost', 5000, debug = True)
