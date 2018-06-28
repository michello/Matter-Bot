from flask import *
# import sms
#from db_connection import *

# for database connection if needed
import os
#import SMSOutgoing
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
# db = MyDB()

'''
conn = pymysql.connect(
  host='localhost',
  port=8080,
  user='root',
  password='',
  db='wms_request_pipeline',
  charset='utf8mb4',
  cursorclass=pymysql.cursors.DictCursor)
'''