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

"""@app.route("/sms", methods=["GET", "POST"])
def sms_reply():
    resp = MessagingResponse()
    #body = request.values.get('Body', None)
    message_body = request.form['Body']
    #for debuging the SMS instercept
    #saveFile = open('bodyfile.txt', 'w')
    #saveFile.write(body)
    #saveFile.close()

    resp.message("Testting the SMS responce")
    return str(resp)
    return str(body)
"""
