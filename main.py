# homepage
# probably where we'll showcase the posts/exchanges that's been made
from flask import *
from appdef import app

import os
from twilio.rest import Client
from slackclient import SlackClient
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

TWILIO_SID = os.environ['TWILIO_SID']
TWILIO_TOKEN = os.environ['TWILIO_TOKEN']
SLACK_TOKEN = os.environ['SLACK_TOKEN']
 
# Create Twilio and Slack REST client object
t_client = Client(TWILIO_SID, TWILIO_TOKEN)
s_client = SlackClient(SLACK_TOKEN)
  
@app.route("/", methods=['GET'])
def main():
    return render_template("index.html")

@app.route("/incoming_sms", methods=['GET', 'POST'])
def incoming_sms():
  # TODO: Make it two way 
  if request.method == 'POST':
    resp = MessagingResponse()
    resp.message("""What is your First Name and Last Name?""")
  
    return str(resp)
  # elif request.method == 'GET':?
    
  
  # if request.method == 'GET':
  #   # Retrieve the message list
  #   message = t_client.messages.list()

  #   for sms in message:
  #     if (sms.to == "+12012989124"):
  #       s_client.api_call(
  #         "chat.postMessage",
  #         channel="recommendations",
  #         text=sms.body
  #       )
  #       return sms.body
  # elif request.method == 'POST':
  #   # Start our TwiML response
  #   resp = MessagingResponse()
  #   resp.message("Ahoy! Thanks so much for your message nnnsd. ")
  #   return str(resp)
  # else:
  #   resp.message("Ahoy! Thanks so much for your message.")
  #   return str(resp)

if __name__ == "__main__":
  app.run(debug=True)