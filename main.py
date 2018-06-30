# homepage
# probably where we'll showcase the posts/exchanges that's been made
from flask import *
from appdef import app, conn

import os
from twilio.rest import Client
from slackclient import SlackClient
from flask import Flask, request, redirect, session
from twilio.twiml.messaging_response import MessagingResponse

import unicodedata

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
employee_id =['07021', '03053', '78534', '01273', '06295', '05217', '37482']
employee_name = ['DANDAN LIN', 'MICHELLE LAM', 'RICHARD WU', 'HUI WAH CHIANG']
employee_title = ['RUNNER', 'ASSOCIATE', 'QA ASSOCIATE', 'KITTER', 'SPECIALIST', 'MACHINE OPERATOR', 'TECH', 'CUSTODIAN']

@app.route("/", methods=['GET'])
def main():
    return render_template("index.html")

@app.route("/incoming_sms", methods=['GET', 'POST'])
def incoming_sms():
  resp = MessagingResponse()

  if request.method == 'POST':
    counter = session.get('counter', 0)
    counter += 1

    # Save the new counter value in the session
    session['counter'] = counter
    message_body = request.values.get('Body', None)

    if message_body == 'HI':
      message = "Thank you " + message_body +", please enter your Employee ID"
    if message_body.find("[emp_id]") != -1:
      message_body = message_body.encode('utf8')
      message = message_body.split()

      employee_id = str(message[1])
      print(employee_id)

      query = "SELECT * FROM Employee WHERE EMPLID='"+employee_id+"'"
      cursor = conn.cursor()
      cursor.execute(query)
      hello = cursor.fetchall()
      cursor.close()
      print("entry: ", hello)

    return str(resp)

if __name__ == "__main__":
  app.secret_key = 'HELLOWORLD'
  app.run('localhost', 5000)
