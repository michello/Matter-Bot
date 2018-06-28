import os
import twilio
import twilio.rest

from flask import *
from flask import request
from appdef import app
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml

from slackclient import SlackClient

# app = Flask(__name__)

slack_token = open("slack_creds.txt","r").readline().strip()
sc = SlackClient(slack_token)


TWILIO_SID = os.environ['TWILIO_SID']
TWILIO_TOKEN = os.environ['TWILIO_TOKEN']

client = Client(TWILIO_SID, TWILIO_TOKEN)

'''
@app.route("/incoming_sms", methods=["POST"])
def inbound_sms():
    response = twiml.Response()
    # we get the SMS message from the request. we could also get the
    # "To" and the "From" phone number as well
    inbound_message = request.form.get("Body")
    # we can now use the incoming message text in our Python application
    if inbound_message == "Hello":
        response.message("Hello back to you!")
    else:
        response.message("Hi! Not quite sure what you meant, but okay.")
    # we return back the mimetype because Twilio needs an XML response
    return Response(str(response), mimetype="application/xml"), 200
'''
@app.route("/incoming_sms", methods=['GET'])
def incoming_sms():
  with app.app_context():
    # messages = client.messages.list()
    # incoming = []

    #number = request.form['From']
    '''
    message_body = request.form['Body']
    print(message_body)

    sc.api_call(
      "chat.postMessage",
      channel="recommendations",
      text=message_body
    )
    '''
    resp = MessagingResponse()
    print(resp)
    '''
    request.form['Body']
    resp = twiml.Response
    print(resp)
    '''
    '''
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
    incoming = []''
    '''
    # Start our TwiML response here
    #resp = MessagingResponse()
