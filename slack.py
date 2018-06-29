import os
from flask import *
from slackclient import SlackClient
from appdef import app
SLACK_TOKEN = os.environ['SLACK_TOKEN']

sc = SlackClient(SLACK_TOKEN)

'''
sc.api_call(
  "chat.postMessage",
  channel="recommendations",
  text="Hello from Python! :tada:"
)
'''

@app.route('/history')
def chatHistory():

  sc_history = sc.api_call(
    "conversations.history",
    channel="CBEDJTJUQ"
  )

  sc_history = sc_history['messages']
  return render_template('friends.html', sc_history=sc_history)
