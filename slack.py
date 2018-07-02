import os
import json
from slackclient import SlackClient

SLACK_TOKEN = os.environ.get('SLACK_TOKEN')

slack_client = SlackClient(SLACK_TOKEN)

# def list_channels():
#     channels_call = slack_client.api_call("channels.list")
#     if channels_call.get('ok'):
#         return channels_call['channels']
#     return None

# def channel_info(channel_id):
#     channel_info = slack_client.api_call("channels.info", channel=channel_id)
#     if channel_info:
#         return channel_info['channel']
#     return None

def findDept(dept):
    if (dept == 'fsqa' or dept == 'kitchen' or dept == 'packing' or dept == 'sanitation' or dept == 'shipping'):
        return dept
    else: return 'other'

def send_message(channel_id, message, eid, urgency, emp_name, idea, why):
    color = #008B00
    if urgency == 5 or urgency == 4
        color = #e50000
    elif urgency == 3:
        color =  #e5e500

    message_attachments = [
        {
            "fallback": idea,
            "author_name": "e_id: " + eid + ", " + emp_name,
            "title": idea,
            "color": color,
            "text": why,
            "actions": [
                {
                    "name": "Accept",
                    "text": "Accept",
                    "type": "button",
                    "value": "yes",
                    "style": "primary"
                },
                {
                    "name": "Decline",
                    "text": "Decline",
                    "type": "button",
                    "value": "no",
                    "style": "danger"
                },
                {
                    "name": "Considering",
                    "text": "Considering",
                    "type": "button",
                    "value": "maybe"
                }
            ]
        }
    ]

    slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='Matter-Bot',
        icon_emoji=':robot_face:',
        attachments=message_attachments
    )
