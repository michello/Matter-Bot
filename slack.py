from slackclient import SlackClient

slack_token = open("slack_creds.txt","r").readline().strip()

sc = SlackClient(slack_token)

'''
sc.api_call(
  "chat.postMessage",
  channel="recommendations",
  text="Hello from Python! :tada:"
)
'''

sc_history = sc.api_call(
  "conversations.history",
  channel="CBEDJTJUQ"
)

print(sc_history['messages'])
