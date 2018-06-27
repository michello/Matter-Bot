#from slackclient import SlackClient

slack_token = open("slack_creds.txt","r").readline().strip()
print(slack_token)

'''
slack_token = os.environ[]
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="C0XXXXXX",
  text="Hello from Python! :tada:"
)
'''
