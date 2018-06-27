import os
import twilio
import twilio.rest

from flask import *
from appdef import app
from twilio.rest import Client

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

  # Just testing
  for record in incoming:
    print record
  
  # Start our TwiML response here
  resp = MessagingResponse()