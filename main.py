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

# @app.route("/", methods=['GET'])
# def main():
#     return render_template("index.html")

@app.route("/incoming_sms", methods=['GET', 'POST'])
def incoming_sms():
  resp = MessagingResponse()
  resp_message = ""

  if request.method == 'POST':
    # counter = session.get('counter', 0)
    # counter += 1

    # Save the new counter value in the session
    # session['counter'] = counter
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
      # session['counter'] = []
    else:
      # Find department of the employee
      cursor_one = conn.cursor()
      dept_query = "SELECT department FROM Employee WHERE EMPLID ='" + C["cookie_emplid"].value +"'"
      cursor_one.execute(dept_query)
      dept = cursor_one.fetchone()
      cursor_one.close()
      #print(dept['department'].encode('utf8'))


      # Find current ticket reviewer

      cursor_three = conn.cursor()
      reviewer_query = "SELECT EMPLID FROM Employee WHERE department ='"+dept['department'].encode('utf8')+"' AND title = 'MANAGER'"
      cursor_three.execute(reviewer_query)
      reviewer = cursor_three.fetchall()
      cursor_three.close()
      print(reviewer)

      """
      # storing the ticket into DB
      print(C["cookie_idea"].value)
      print(C["cookie_why"].value)
      print(C["cookie_urgency"].value)
      print(reviewer)
      """

      '''
      # storing the ticket into the DB
      cursor_two = conn.cursor()
      query = 'INSERT INTO Ticket (idea, why, urgency, person_in_charge, date_created) VALUES (%s, %s, %s, %s)'
      time = datetime.now()
      cursor_two.execute(query, (C["cookie_idea"].value, C["cookie_why"].value, C["cookie_urgency"].value, reviewer['EMPLID'], time))
      conn.commit()
      cursor_two.close()
      '''


  resp.message(resp_message)
  return str(resp)

if __name__ == "__main__":
  app.secret_key = os.environ["SECRET_KEY"]
  app.run('localhost', 5000)


