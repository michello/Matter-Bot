import os
import pymysql
import pymysql.cursors

from flask import *
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

SECRET_KEY = "HELLO WORLD"#os.environ['SECRET_KEY']

app = Flask(__name__)
# db = MyDB()

conn = pymysql.connect(
   host='localhost',
   user='root',
   password='',
   db='wms_request_pipeline',
   charset='utf8mb4',
   cursorclass=pymysql.cursors.DictCursor)

'''
if (conn):
  #query = 'INSERT INTO Employee VALUES(30000,"ssd","ssd","ssd","ssd"
  query = "SELECT * FROM Employee"
  cursor = conn.cursor()
  cursor.execute(query)
  hello = cursor.fetchall()
  cursor.close()
  print("entry: ", hello)
else:
  print("not connected")
'''

'''




'''
