import os
import pymysql
import pymysql.cursors

from flask import *
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

SECRET_KEY = os.environ['SECRET_KEY']

app = Flask(__name__)
# db = MyDB()

# conn = pymysql.connect(
#   host='localhost',
#   user='root',
#   password='',
#   db='wms_request_pipeline',
#   charset='utf8mb4',
#   cursorclass=pymysql.cursors.DictCursor)
