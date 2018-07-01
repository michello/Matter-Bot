# homepage
# probably where we'll showcase the posts/exchanges that's been made
import os
import twilio.twiml
import Cookie

from twilio import twiml
from appdef import app, conn
from twilio.rest import Client
from slackclient import SlackClient
from datetime import datetime, timedelta
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect, session, make_response

import unicodedata

import datetime

app = Flask(__name__)
app.config.from_object(__name__)

#SECRET_KEY = os.environ['SECRET_KEY']
#SLACK_TOKEN = os.environ['SLACK_TOKEN']

TWILIO_SID = os.environ['TWILIO_SID']
TWILIO_TOKEN = os.environ['TWILIO_TOKEN']

# Create Twilio and Slack REST client object
t_client = Client(TWILIO_SID, TWILIO_TOKEN)
#s_client = SlackClient(SLACK_TOKEN)

urgency = ['1', '2', '3', '4', '5']
department = ['KITCHEN', 'PACKING', 'SANITATION', 'SHIPPING', 'FSQA']
employee_title = ['RUNNER', 'ASSOCIATE', 'QA ASSOCIATE', 'KITTER', 'SPECIALIST', 'MACHINE OPERATOR', 'TECH', 'CUSTODIAN']

C = Cookie.SimpleCookie()

@app.route("/", methods=['GET'])
def main():
    return render_template("index.html")

@app.route("/incoming_sms", methods=['GET', 'POST'])
def incoming_sms():
  resp = MessagingResponse()
  resp_message = ""

  if request.method == 'POST':
    counter = session.get('counter', 0)
    # counter += 1

    # Save the new counter value in the session
    session['counter'] = counter
    message_body = request.values.get('Body', None)
    message_body = message_body.encode('utf8')

    if message_body.upper() == 'HI':
      resp_message = "Thank you " + message_body +", please enter your Employee ID"

    if message_body.find("[emp_id]") != -1:
      message_body = message_body.encode('utf8')
      message = message_body.split()

      employee_id = str(message[1])


      query = "SELECT * FROM Employee WHERE EMPLID='"+employee_id+"'"
      cursor = conn.cursor()
      cursor.execute(query)
      user = cursor.fetchall()
      cursor.close()

      C["cookie_emplid"] = employee_id

      if (len(user) == 1):
        resp_message = "What is the Level of urgency? (1-5)"
      else:
        resp_message = "Please enter a valid Blue Apron ID"

    if message_body in urgency:
      C["cookie_urgency"] = int(message_body)
      resp_message = "Which department do you belong to?"

    if message_body.upper() in department:
      C["cookie_department"] = message_body
      resp_message = "What is your job title?"

    if message_body.upper() in employee_title:
      C["cookie_title"] = message_body
      resp_message = "Thank you. You now can share your idea with us \nSend \'Done\' when you finish"

    if message_body.upper() == "DONE":
      C["cookie_body"] = message_body
      resp_message = "Thank you for using Matter Bot. Have a great day"
      session['counter'] = []

      # storing the ticket into DB
      cursor = conn.cursor()
      query = 'INSERT INTO Ticket (idea, urgency, date_created) VALUES (%s, %s, %s)'
      time = datetime.datetime.now()
      cursor.execute(query, (C["cookie_body"].value, C["cookie_urgency"].value, time))
      conn.commit()
      cursor.close()



  # print (C)

  resp.message(resp_message)
  return str(resp)

if __name__ == "__main__":
  app.secret_key = 'HELLOWORLD'
  app.run('localhost', 5000)


