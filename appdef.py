from flask import *
import sms
import pymysql.cursors

# for database connection if needed

app = Flask(__name__)
conn = pymysql.connect(
  host='localhost',
  port=8080,
  user='root',
  password='',
  db='wms_request_pipeline',
  charset='utf8mb4',
  cursorclass=pymysql.cursors.DictCursor)


while (True):
  sms.incoming_sms()
