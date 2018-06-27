from flask import Flask, render_template
from appdef import app
## each page will have its own python file/module, which will be imported from here:
import main, slack

if __name__ == "__main__":
    app.run('localhost', 5000, debug = True)
