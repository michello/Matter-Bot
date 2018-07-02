# homepage
# probably where we'll showcase the posts/exchanges that's been made
import os
import Cookie
import datetime
import unicodedata
import twilio.twiml

from twilio import twiml
from appdef import app, conn
from twilio.rest import Client
from slackclient import SlackClient
from datetime import datetime, timedelta
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect, session, make_response

from google_sheets import *
from google_sheets import insert

from slack import *
from slack import send_message, findDept

app = Flask(__name__)
app.config.from_object(__name__)

SECRET_KEY = os.environ['SECRET_KEY']
#SLACK_TOKEN = os.environ['SLACK_TOKEN']

TWILIO_SID = os.environ['TWILIO_SID']
TWILIO_TOKEN = os.environ['TWILIO_TOKEN']

# Create Twilio and Slack REST client object
t_client = Client(TWILIO_SID, TWILIO_TOKEN)
#s_client = SlackClient(SLACK_TOKEN)

urgency = ['1', '2', '3']
department = ['KITCHEN', 'PACKING', 'SANITATION', 'SHIPPING', 'FSQA']
employee_title = ['RUNNER', 'ASSOCIATE', 'QA ASSOCIATE', 'KITTER', 'SPECIALIST', 'MACHINE OPERATOR', 'TECH', 'CUSTODIAN']

C = Cookie.SimpleCookie()

@app.route("/incoming_sms", methods=['GET', 'POST'])
def incoming_sms():
  resp = MessagingResponse()
  resp_message = ""

  if request.method == 'POST':
    message_body = request.values.get('Body', None)
    message_body = message_body.encode('utf8')

    if message_body.upper() == 'IDEA':
      resp_message = "Welcome! We're excited bout your idea! Let's get started. Please type your EID and begin with 'EID: '"

    elif "EID: " in message_body.upper():

      message = message_body.split()

      employee_id = str(message[1])

      query = "SELECT * FROM Employee WHERE EMPLID='"+employee_id+"'"
      cursor = conn.cursor()
      cursor.execute(query)
      user = cursor.fetchall()
      cursor.close()

      C["cookie_emplid"] = employee_id

      if (len(user) == 1):
        resp_message = "Thanks! From 1-3, how urgent is your idea? 1 being the least urgent."
      else:
        resp_message = "Please enter a valid Blue Apron ID."

    elif message_body in urgency:
      C["cookie_urgency"] = int(message_body)
      resp_message = "Got it. In a sentence, please describe your idea. 'My idea is...'"

    elif "MY IDEA IS" in message_body.upper():
      C["cookie_idea"] = message_body
      resp_message = "Last part: How did you come up with your idea and why is it worth pursuing? 'I came up with this idea because...'"

    elif "I CAME UP WITH THIS IDEA BECAUSE" in message_body.upper():
      C["cookie_why"] = message_body
      resp_message = "Thank you for using Matter Bot. Please send 'Done' when you're finished and have a great day!"

    else:
      # Find department of the employee
      cursor_one = conn.cursor()
      dept_query = "SELECT department FROM Employee WHERE EMPLID ='" + C["cookie_emplid"].value +"'"
      cursor_one.execute(dept_query)
      dept = cursor_one.fetchone()
      cursor_one.close()

      # Find current ticket reviewer
      cursor_three = conn.cursor()
      reviewer_query = "SELECT EMPLID FROM Employee WHERE department ='"+dept['department'].encode('utf8')+"' AND title = 'MANAGER'"
      cursor_three.execute(reviewer_query)
      reviewer = cursor_three.fetchone()
      cursor_three.close()

      # storing the ticket into the DB
      cursor_two = conn.cursor()
      query = 'INSERT INTO ticket (idea, why, urgency, date_created, person_in_charge) VALUES (%s, %s, %s, %s, %s);'
      time = datetime.now()
      cursor_two.execute(query, (C["cookie_idea"].value, C["cookie_why"].value, int(C["cookie_urgency"].value), time, reviewer['EMPLID']))
      conn.commit()
      cursor_two.close()

      # getting the tracking id to insert to google sheets later
      cursor_four = conn.cursor()
      trackingNo_query = "SELECT ticket_id FROM ticket WHERE IDEA ='" + C["cookie_idea"].value +"'"
      cursor_four.execute(trackingNo_query)
      trackingNo = cursor_four.fetchone()
      cursor_four.close()

      # insert into google sheets
      insert(C["cookie_emplid"].value, C["cookie_urgency"].value, C["cookie_idea"].value, C["cookie_why"].value, trackingNo['ticket_id'])

      # slack integration
      channel_id = findDept(dept["department"])

      # find person name
      cursor_five = conn.cursor()
      emp_query = "SELECT employee_name FROM Employee WHERE EMPLID ='" + C["cookie_emplid"].value +"'"
      cursor_five.execute(emp_query)
      emp_name = cursor_five.fetchone()
      cursor_five.close()

      # find person groupname
      cursor_six = conn.cursor()
      group_query = "SELECT groupname FROM Employee WHERE EMPLID ='" + C["cookie_emplid"].value +"'"
      cursor_six.execute(group_query)
      group = cursor_six.fetchone()
      cursor_six.close()

      # sending message to slack
      send_message(channel_id, "Department " + channel_id + " " + group["groupname"], C["cookie_emplid"].value, int(C["cookie_urgency"].value), emp_name["employee_name"], C["cookie_idea"].value, C["cookie_why"].value)

  resp.message(resp_message)
  return str(resp)

if __name__ == "__main__":
  app.secret_key = os.environ["SECRET_KEY"]
  app.run('localhost', 5000)


