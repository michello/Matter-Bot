import os
import json
from flask import *
from slackclient import SlackClient
from appdef import app

SLACK_TOKEN = os.environ.get('SLACK_TOKEN')

slack_client = SlackClient(SLACK_TOKEN)

def list_channels():
    channels_call = slack_client.api_call("channels.list")
    if channels_call.get('ok'):
        return channels_call['channels']
    return None

def channel_info(channel_id):
    channel_info = slack_client.api_call("channels.info", channel=channel_id)
    if channel_info:
        return channel_info['channel']
    return None

eid = "12345"
facility = "Linden"
first_name = "Bob"
shift = "7am - 7pm"
def urgency(urgent):
    if urgent == "urgent":
        return #e50000
    elif urgent == "moderate":
        return #e5e500
    else: return #008B00

message_attachments = [
    {
        "fallback": "Idea: Give employees super suits",
        "author_name": "e_id: " + eid + ", " + first_name,
        "title": "Idea: Give employees super suits",
        "color": "#008B00",
        "text": "Why: The freezer area is too cold.",
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

def send_message(channel_id, message):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='Matter-Bot',
        icon_emoji=':robot_face:',
        attachments=message_attachments
    )

if __name__ == '__main__':
    channels = list_channels()
    if channels:
        print("Channels: ")
        for channel in channels:
            print(channel['name'] + " (" + channel['id'] + ")")
            if channel['name'] == 'testing':
                send_message(channel['id'], "Department " + 
                             channel['name'] + ", " + shift)
        print('-----')

    else:
        print("Unable to authenticate.")
