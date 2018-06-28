from appdef import app
from twilio.rest import Client
import os

TWILIO_SID = os.environ['TWILIO_SID']
TWILIO_TOKEN = os.environ['TWILIO_TOKEN']

while True:
  client = Client(TWILIO_SID, TWILIO_TOKEN)
  messages = client.messages.list()
  for msg in messages:
    print(msg.body)
  #print(messages['body'])
  #time.sleep(5)
