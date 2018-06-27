from flask import *
from slackclient import SlackClient
from appdef import app
slack_token = open("slack_creds.txt","r").readline().strip()

sc = SlackClient(slack_token)

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
