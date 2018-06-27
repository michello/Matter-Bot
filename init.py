from flask import Flask, render_template
from appdef import app
import main

if __name__ == "__main__":
    app.run('localhost', 5000, debug = True)
