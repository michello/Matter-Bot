# homepage
# probably where we'll showcase the posts/exchanges that's been made
from flask import *
from appdef import app

import os
from twilio.rest import Client
from slackclient import SlackClient
from flask import Flask, request, redirect, session
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
app.config.from_object(__name__)

SECRET_KEY = os.environ['SECRET_KEY']
SLACK_TOKEN = os.environ['SLACK_TOKEN']

TWILIO_SID = os.environ['TWILIO_SID']
TWILIO_TOKEN = os.environ['TWILIO_TOKEN']

# Create Twilio and Slack REST client object
t_client = Client(TWILIO_SID, TWILIO_TOKEN)
s_client = SlackClient(SLACK_TOKEN)

employee_name = ['DANDAN LIN', 'MICHELLE LAM', 'RICHARD WU', 'HUI WAH CHIANG']
employee_id =['0702', '0305', '7853', '0127', '0629', '0521']
job_title = ['RUNNER', 'ASSOCIATE', 'QA ASSOCIATE', 'KITTER', 'SPECIALIST', 'MACHINE OPERATOR', 'TECH', 'CUSTODIAN']

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
    message_from = request.values.get('From')
    message_body = request.values.get('Body').upper()

    message = ''

    if message_body == 'HI':
      message = 'Hi, what is your First Name and Last Name?'
    elif message_body in employee_name :
      message = "Thank you " + message_body +", please enter your Employee ID"
    elif message_body in employee_id:
      message = "What is your job title?"
    elif message_body in job_title:
      message = "Thank you. You now can share your idea with us \nSend \'Done\' when you finish"
    elif message_body == 'DONE':
      message = "Thank you for using Matter Bot. Have a great day"
    # else:
      # TODO: where to save the data?


    resp.message(message)
    return str(resp)

if __name__ == "__main__":
  app.secret_key = SECRET_KEY
  app.run(debug=True)
  app.run()