import os
import twilio
import twilio.rest

from flask import *
from appdef import app
from twilio.rest import Client

from slackclient import SlackClient

app = Flask(__name__)

slack_token = open("slack_creds.txt","r").readline().strip()
sc = SlackClient(slack_token)


TWILIO_SID = os.environ['TWILIO_SID']
TWILIO_TOKEN = os.environ['TWILIO_TOKEN']

client = Client(TWILIO_SID, TWILIO_TOKEN)

@app.route("/incoming_sms", methods=['GET', 'POST'])
def incoming_sms():
  messages = client.messages.list()
  incoming = []

  for sms in client.messages.list():
    if (sms.to == "+12012989124"):
      incoming.append(sms.body)

  for record in incoming:
    print(record)
    sc.api_call(
      "chat.postMessage",
      channel="recommendations",
      text=record
    )
  incoming = []

  # Start our TwiML response here
  resp = MessagingResponse()
